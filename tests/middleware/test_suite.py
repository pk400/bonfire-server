import unittest

from tests.middleware.session_middleware_tester import SessionMiddlewareTester


def suite():
  suite = unittest.TestSuite()
  suite.addTests(unittest.makeSuite(SessionMiddlewareTester))
  return suite


if __name__ == '__main__':
  runner = unittest.TextTestRunner()
  runner.run(suite())
