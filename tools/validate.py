"""Validate the public task packages without any private platform dependencies."""
import hashlib
import json
from pathlib import Path

import jsonschema

root = Path(__file__).resolve().parents[1]
schema = json.loads((root / 'schema/task-v1.schema.json').read_text(encoding='utf-8'))
count = 0
for path in sorted((root / 'tasks').glob('*/task.json')):
    task = json.loads(path.read_text(encoding='utf-8'))
    jsonschema.validate(task, schema)
    for name, checksum in task['assets'].items():
        asset = (path.parent / name).resolve()
        assert asset.is_relative_to(path.parent.resolve()), 'Unsafe asset path'
        assert hashlib.sha256(asset.read_bytes()).hexdigest() == checksum, f'Checksum mismatch: {asset}'
    count += 1
    print('valid', task['task_id'], task['task_version'])
assert count, 'No task packages found'
print(f'{count} task packages validated')
