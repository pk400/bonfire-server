import unittest

from tests.accounts.create_account_tester import CreateAccountTester
from tests.accounts.login_tester import LoginTester


def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(CreateAccountTester))
  suite.addTests(unittest.makeSuite(LoginTester))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
