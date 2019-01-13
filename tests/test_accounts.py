import unittest

from server.accounts import Account, LocalDataStore

class TestAccounts(unittest.TestCase):
  def test_create_account(self):
    account = Account(123, 'a', 'p', 'e')
    self.assertEqual(account.id, 123)
    self.assertEqual(account.username, 'a')
    self.assertEqual(account.password, 'p')
    self.assertEqual(account.email_address, 'e')
  
  def test_accounts_datastore(self):
    ds = LocalDataStore()
    account = Account(0, 'a', 'p', 'e')
    ds.store_account(account)
    ds_account = ds.load_account(0)
    self.assertEqual(account.id, ds_account.id)
    self.assertEqual(account.username, ds_account.username)
    self.assertEqual(account.password, ds_account.password)
    self.assertEqual(account.email_address, ds_account.email_address)
  
if __name__ == '__main__':
  unittest.main()
