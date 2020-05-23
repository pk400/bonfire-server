import unittest

from bonfire.library.accounts.local_data_store import LocalDataStore
from bonfire.library.accounts.server import Server
from bonfire.library.accounts.session import Session
from bonfire.library.utils import run_in_loop
from tests.test_password_hasher import TestPasswordHasher


class TestCreateAccount(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store, TestPasswordHasher())
    server.open()
    session = Session()
    account_id = run_in_loop(server.create_account(session, 'a', 'b'))
    account = run_in_loop(data_store.load_account(account_id))
    self.assertEqual(account.id, 0)
    self.assertEqual(account.email_address, 'a')
    server.close()


if __name__ == '__main__':
  unittest.main()
