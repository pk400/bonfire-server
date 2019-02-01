import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
    '..')))
    
from starlette.testclient import TestClient

from bonfire.app import BonfireApplication
from bonfire.local_database import LocalDataBase

class TestAsgi(unittest.TestCase):
  def setUp(self):
    self.database = LocalDataBase()
    self.client = TestClient(BonfireApplication(self.database))

  def load_user(self):
    account = dict(username='a', email_address='a@astraea.systems',
                   password='pass')
    self.client.post('/register', json=account)

  def test_register_and_login(self):
    account = dict(username='joel', email_address='joel@astraea.systems',
                   password='pass')
    response = self.client.post('/register', json=account)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.text, account['username'])
    account = dict(username='joel', password='pass')
    response = self.client.post('/login', json=account)
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.text, 'Logged in!')
    self.assertEqual(response.cookies['account'], account['username'])
  
  def test_webfinger(self):
    self.load_user()
    params = dict(resource='a@astraea.systems')
    response = self.client.get('/.well-known/webfinger', params=params)
    print(response)
  
  def test_users(self):
    self.load_user()
    response = self.client.get('/users/a')
    
if __name__ == '__main__':
  unittest.main()
