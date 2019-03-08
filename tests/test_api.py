import unittest

from bonfire.api import Api

class TestApi(unittest.TestCase):
  def test_register(self):
    api = Api()
    api.open()
    account = {
      'username': 'a',
      'password': 'p'
    }
    api.register(account['username'], account['password'])
    account_found = api.find_account(account['username'])
    self.assertEqual(account_found, account)

if __name__ == '__main__':
  unittest.main()

