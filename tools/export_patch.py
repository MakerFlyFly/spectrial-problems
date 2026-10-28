"""Export UTF-8 Git diff bytes, including staged new files, without shell redirection."""
import argparse
import json
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()
parser.add_argument('--task', required=True)
parser.add_argument('--repo', required=True, type=Path)
parser.add_argument('--output', type=Path, default=Path('solution.patch'))
args = parser.parse_args()
bank = Path(__file__).resolve().parents[1]
packages = {path.parent.name: path for path in (bank / 'tasks').glob('*/task.json')}
if args.task not in packages:
    raise SystemExit('Unknown task')
task = json.loads(packages[args.task].read_text(encoding='utf-8'))
untracked = subprocess.check_output(['git', '-C', str(args.repo), 'ls-files', '--others', '--exclude-standard', '--', *task['allowed_paths']])
if untracked.strip():
    raise SystemExit('New source files are untracked. Run git add on the intended source files first, then export again.')
patch = subprocess.check_output(['git', '-C', str(args.repo), '-c', 'core.quotePath=false',
                                 'diff', '--binary', task['base_commit'], '--', *task['allowed_paths']])
if not patch.strip():
    raise SystemExit('No source changes found relative to the task base commit')
args.output.write_bytes(patch)
print(f'Exported {len(patch)} bytes to {args.output.resolve()}')
