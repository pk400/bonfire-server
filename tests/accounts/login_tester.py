import unittest

from backend.accounts.account import Account
from backend.accounts.local_data_store import LocalDataStore
from backend.accounts.server import Server
from backend.accounts.session import Session
from backend.utils import run_in_loop

class LoginTester(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store)
    server.open()
    run_in_loop(server.create_account('a', 'b'))
    run_in_loop(server.login(Session(), 'a', 'b'))
    server.close()

if __name__ == '__main__':
  unittest.main()
