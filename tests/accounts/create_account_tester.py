import unittest

from library.accounts.local_data_store import LocalDataStore
from library.accounts.server import Server
from library.password_hasher.test_password_hasher import TestPasswordHasher
from library.utils import run_in_loop


class CreateAccountTester(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store, TestPasswordHasher())
    server.open()
    account_id = run_in_loop(server.create_account('a', 'b'))
    account = run_in_loop(data_store.load_account(account_id))
    self.assertEqual(account.id, 0)
    self.assertEqual(account.email_address, 'a')
    server.close()


if __name__ == '__main__':
  unittest.main()
