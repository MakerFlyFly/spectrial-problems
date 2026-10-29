"""Public grading checks require only the Python standard library."""
from pathlib import Path
import sys
import unittest

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'tools'))
from grading import grade, PARSER_VERSION, PYTHON_V2


class GradingChecks(unittest.TestCase):
    def test_v1_compatibility(self):
        task={'log_parser':'parse_log_requests','fail_to_pass':['test[/foo]'],'pass_to_pass':['old']}
        result=grade(task,'PASSED test[/path/foo]\nPASSED old')
        self.assertEqual(result['verdict'],'passed')
        self.assertEqual(result['parser_version'],PARSER_VERSION)

    def test_django(self):
        task={'environment':{'parser_version':PYTHON_V2},'log_parser':'parse_log_django','fail_to_pass':['test_fix (suite.Case)'],'pass_to_pass':['test_old (suite.Case)']}
        self.assertEqual(grade(task,'test_fix (suite.Case) ... ok\ntest_old (suite.Case) ... ok')['verdict'],'passed')
        self.assertEqual(grade(task,'test_fix (suite.Case) ... FAIL\ntest_old (suite.Case) ... ok')['verdict'],'failed')

    def test_sphinx_both_status_positions_and_missing_results(self):
        task={'environment':{'parser_version':PYTHON_V2},'log_parser':'parse_log_sphinx','fail_to_pass':['a::fix'],'pass_to_pass':['a::old']}
        self.assertEqual(grade(task,'a::fix PASSED\nPASSED a::old')['verdict'],'passed')
        self.assertEqual(grade(task,'PASSED a::fix')['verdict'],'failed')

    def test_unknown_version_rejected(self):
        with self.assertRaises(ValueError):
            grade({'environment':{'parser_version':'unknown'},'log_parser':'parse_log_django'},'')


if __name__=='__main__':unittest.main()
