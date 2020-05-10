import unittest

from server import exceptions
from services.accounts.local_data_store import LocalDataStore
from services.accounts.server import Server
from services.accounts.session import Session
from types import TestPasswordHasher
from utils import run_in_loop


class LoginTester(unittest.TestCase):
  def setUp(self):
    self.data_store = LocalDataStore()
    self.server = Server(self.data_store, TestPasswordHasher())
    self.server.open()
    run_in_loop(self.server.create_account('a', 'b'))

  def tearDown(self):
    self.server.close()

  def test_success(self):
    result = run_in_loop(self.server.login(Session(), 'a', 'b'))
    self.assertTrue(result)

  def test_bad_credentials(self):
    with self.assertRaises(exceptions.BadCredentialsException):
      run_in_loop(self.server.login(Session(), 'a', 'z'))

  def test_already_logged_in(self):
    session = Session()
    run_in_loop(self.server.login(session, 'a', 'b'))
    with self.assertRaises(exceptions.SessionLoggedInException):
      run_in_loop(self.server.login(session, 'a', 'b'))


if __name__ == '__main__':
  unittest.main()
