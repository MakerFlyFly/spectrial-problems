"""Pytest adapters and F2P/P2P semantics adapted from SWE-bench (MIT).

Upstream: SWE-bench/SWE-bench@02e7a74ffd0b707aab73d203fe87bdc7c76afc8e
swebench/harness/log_parsers/python.py and harness/grading.py.
See THIRD_PARTY_NOTICES.md for attribution and license.
Only the two parser variants required by the curated tasks are supported.
"""
import re

PARSER_VERSION = 'swebench-02e7a74-pytest-v1'
STATUSES = ('PASSED', 'FAILED', 'SKIPPED', 'ERROR', 'XFAIL')


def parse_tests(log: str, parser: str) -> dict[str, str]:
    if parser not in ('parse_log_flask', 'parse_log_requests', 'parse_log_pytest'):
        raise ValueError('Unsupported test log parser')
    statuses = {}
    log = re.sub(r'\x1b\[[0-9;]*[a-zA-Z]', '', log)
    for line in log.splitlines():
        if not any(line.startswith(value + ' ') for value in STATUSES):
            continue
        if line.startswith('FAILED'):
            line = line.replace(' - ', ' ')
        parts = line.split()
        if len(parts) < 2:
            continue
        status, name = parts[:2]
        if status == 'SKIPPED' and re.fullmatch(r'\[\d+\]', name):
            continue
        if parser == 'parse_log_requests':
            option = re.search(r'(.*?)\[(.*)\]', name)
            if option:
                main, value = option.groups()
                if value.startswith('/') and not value.startswith('//') and '*' not in value:
                    value = '/' + value.split('/')[-1]
                name = f'{main}[{value}]'
        statuses[name] = status
    return statuses


def grade(manifest: dict, log: str) -> dict:
    if '>>>>> Start Test Output' in log:
        log = log.split('>>>>> Start Test Output', 1)[1]
    if '>>>>> End Test Output' in log:
        log = log.split('>>>>> End Test Output', 1)[0]
    actual = parse_tests(log, manifest['log_parser'])
    tests = []
    for group, key in [('修复测试', 'fail_to_pass'), ('回归测试', 'pass_to_pass')]:
        for name in manifest[key]:
            tests.append({'id': name, 'group': group, 'status': actual.get(name, 'NOT_RUN')})
    passed = sum(test['status'] == 'PASSED' for test in tests)
    resolved = bool(manifest['fail_to_pass']) and passed == len(tests)
    return {'verdict': 'passed' if resolved else 'failed', 'passed': passed, 'total': len(tests),
            'tests': tests, 'parser_version': PARSER_VERSION,
            'message': '全部修复测试与回归测试通过。' if resolved else '部分固定测试尚未通过，请查看测试报告。'}
