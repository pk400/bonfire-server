import unittest

from server.accounts import Account

class TestAccounts(unittest.TestCase):
  def test_create_account(self):
    account = Account(123, 'a', 'p', 'e')
    self.assertEqual(account.id, 123)
    self.assertEqual(account.username, 'a')
    self.assertEqual(account.password, 'p')
    self.assertEqual(account.email_address, 'e')

if __name__ == '__main__':
  unittest.main()
