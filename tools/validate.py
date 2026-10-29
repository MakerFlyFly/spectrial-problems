"""Validate the public task packages without any private platform dependencies."""
import hashlib
import json
from pathlib import Path

import jsonschema

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / 'schema/task-v1.schema.json').read_text(encoding='utf-8'))
count = 0
packages = {}
for path in sorted((root / 'tasks').glob('*/task.json')):
    task = json.loads(path.read_text(encoding='utf-8'))
    assert path.parent.name==task['task_id'], 'Task directory and identity differ'
    jsonschema.validate(task, schema)
    for name, checksum in task['assets'].items():
        asset = (path.parent / name).resolve()
        assert asset.is_relative_to(path.parent.resolve()), 'Unsafe asset path'
        assert hashlib.sha256(asset.read_bytes()).hexdigest() == checksum, f'Checksum mismatch: {asset}'
    if 'upstream-eval.sh' in task['assets']:
        original=(path.parent/'upstream-eval.sh').read_bytes()
        assert (path.parent/'eval.sh').read_bytes()==original.replace(b' -v -- ',b' -v -- -rA '), 'Unexpected upstream script modification'
    count += 1
    packages[task['task_id']] = (task,path.parent)
    print('valid', task['task_id'], task['task_version'])
assert count, 'No task packages found'
metadata=root/'release.json'
if metadata.exists():
    assert json.loads(metadata.read_text(encoding='utf-8'))['task_count']==count
summary=root/'validation-summary.json'
if summary.exists():
    receipts=json.loads(summary.read_text(encoding='utf-8'))['tasks']
    assert {r['task_id'] for r in receipts}==set(packages), 'Receipt coverage differs from catalog'
    for receipt in receipts:
        task,directory=packages[receipt['task_id']]
        canonical=dict(task,_evaluation=(directory/'eval.sh').read_text(encoding='utf-8'),_statement=(directory/'problem.md').read_text(encoding='utf-8'))
        digest=hashlib.sha256(json.dumps(canonical,sort_keys=True,ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
        assert digest==receipt['package_sha256'], 'Receipt package digest mismatch'
        runs=receipt['runs']
        assert len(runs)==3 and [r['kind'] for r in runs]==['baseline','gold','gold']
        assert all(r['valid'] for r in runs)
        total=len(task['fail_to_pass'])+len(task['pass_to_pass'])
        assert runs[0]['verdict']=='failed' and runs[0]['passed']==len(task['pass_to_pass']) and runs[0]['total']==total
        assert all(r['verdict']=='passed' and r['passed']==r['total']==total for r in runs[1:])
print(f'{count} task packages validated')
