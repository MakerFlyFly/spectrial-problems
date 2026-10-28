"""Run the same fixed tests with Docker; no private platform or platform account needed."""
import argparse
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile
import shlex
import sys
from grading import grade

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

parser = argparse.ArgumentParser()
parser.add_argument('--task', required=True)
parser.add_argument('--patch', required=True, type=Path)
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
packages = {path.parent.name: path.parent for path in (root / 'tasks').glob('*/task.json')}
if args.task not in packages:
    raise SystemExit('Unknown task')
package = packages[args.task]
task = json.loads((package / 'task.json').read_text(encoding='utf-8'))
image = task['environment']['image']
subprocess.run(['docker', 'pull', image], check=True)
command = 'git -C /testbed reset --hard ' + shlex.quote(task['base_commit']) + ' && git -C /testbed clean -fd'
if args.patch.read_bytes().strip():
    command += ' && git -C /testbed apply /tmp/solution.patch'
command += ' && bash /tmp/eval.sh'
cid = subprocess.check_output(['docker', 'create', '--platform', 'linux/amd64', '--network', 'none',
    '--memory', '3g', '--memory-swap', '3g', '--cpus', '2', '--pids-limit', '256',
    '--cap-drop', 'ALL', '--security-opt', 'no-new-privileges',
    '--env', 'PIP_NO_INDEX=1', '--env', 'PIP_NO_BUILD_ISOLATION=1', '--env', 'OPENBLAS_NUM_THREADS=1',
    '--entrypoint', '/bin/bash', image, '-c', command]).decode().strip()
try:
    subprocess.run(['docker', 'cp', str(args.patch.resolve()), cid + ':/tmp/solution.patch'], check=True)
    subprocess.run(['docker', 'cp', str((package / 'eval.sh').resolve()), cid + ':/tmp/eval.sh'], check=True)
    # Preserve stream order: the official start/end markers are written to stderr.
    result = subprocess.run(['docker', 'start', '-a', cid], timeout=600,
                            stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    log = result.stdout.decode('utf-8', errors='replace')
    print(log)
    report = grade(task, log)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    raise SystemExit(0 if report['verdict'] == 'passed' else 1)
finally:
    subprocess.run(['docker', 'rm', '-f', cid], check=False, stdout=subprocess.DEVNULL)
