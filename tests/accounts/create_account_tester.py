import asyncio
import unittest

from backend.accounts import LocalDataStore, Server
from backend.utils import run_in_loop

class CreateAccountTester(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store)
    server.open()
    account_id = run_in_loop(server.create_account('a', 'b'))
    account = run_in_loop(data_store.load_account(account_id))
    self.assertEqual(account.id, 0)
    self.assertEqual(account.email_address, 'a')
    server.close()

if __name__ == '__main__':
  unittest.main()
