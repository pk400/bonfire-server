import unittest

from bonfire.library import exceptions
from bonfire.library.accounts.local_data_store import LocalDataStore
from bonfire.library.accounts.server import Server
from bonfire.library.accounts.session import Session
from bonfire.library.utils import run_in_loop
from tests.test_password_hasher import TestPasswordHasher


class LoginTester(unittest.TestCase):
  def setUp(self):
    self.data_store = LocalDataStore()
    self.server = Server(self.data_store, TestPasswordHasher())
    self.server.open()

  def tearDown(self):
    self.server.close()

  def test_success(self):
    session = Session()
    account_id = run_in_loop(self.server.create_account(session, 'a', 'b'))
    run_in_loop(self.server.login(session, 'a', 'b'))
    self.assertTrue(session.is_modified)
    self.assertEqual(session.id, account_id)

  def test_bad_credentials(self):
    session = Session()
    account_id = run_in_loop(self.server.create_account(session, 'a', 'b'))
    run_in_loop(self.server.login(session, 'a', 'b'))
    self.assertTrue(session.is_modified)
    self.assertEqual(session.id, account_id)
    with self.assertRaises(exceptions.SessionLoggedInException):
      run_in_loop(self.server.login(session, 'a', 'b'))


if __name__ == '__main__':
  unittest.main()
