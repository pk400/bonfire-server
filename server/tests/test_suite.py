import unittest

from tests.accounts.test_suite import suite as AccountsTestSuite
from tests.accounts.test_suite import suite as MiddlewareTestSuite


def suite():
  suite = unittest.TestSuite()
  suite.addTests(AccountsTestSuite())
  suite.addTests(MiddlewareTestSuite())
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
