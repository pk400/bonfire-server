import unittest

from backend.accounts.local_data_store import LocalDataStore
from backend.accounts.server import Server

class LoginTester(unittest.TestCase):
  def test_success(self):
    data_store = LocalDataStore()
    server = Server(data_store)
    server.open()
    server.close()

if __name__ == '__main__':
  unittest.main()