import unittest

from tests.accounts.test_suite import suite as AccountsTestSuite
from tests.middleware.test_suite import suite as MiddlewareTestSuite
from tests.multi_key_dict_tester import MultiKeyDictTester


def suite():
  suite = unittest.TestSuite()
  suite.addTests(AccountsTestSuite())
  suite.addTests(MiddlewareTestSuite())
  suite.addTests(unittest.makeSuite(MultiKeyDictTester))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
