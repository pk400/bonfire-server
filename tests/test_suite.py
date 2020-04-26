import unittest

from tests.accounts.test_suite import suite as AccountsTestSuite


def suite():
  suite = unittest.TestSuite()
  suite.addTests(AccountsTestSuite())
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
