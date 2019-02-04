import json
import os
import sys
import unittest
    
from starlette.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
  '..')))
from bonfire import BonfireApplication, LocalDataBase

class TestAsgi(unittest.TestCase):
  def setUp(self):
    self.url = os.environ['BONFIRE_URL']
    self.database = LocalDataBase(self.url)
    self.client = TestClient(BonfireApplication(self.database))

  def load_user(self):
    account = dict(username='a', password='pass')
    self.client.post('/register', json=account)
    account_in_db = self.database.load_account(account['username'])
    self.assertEqual(account_in_db.username, account['username'])
    self.assertEqual(account_in_db.password, account['password'])

  def test_register_and_login(self):
    account = dict(username='joel', password='pass')
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
    account_address = '@'.join(['a', self.url.split('//')[1]])
    params = dict(resource=':'.join(['acct', account_address]))
    response = self.client.get('/.well-known/webfinger', params=params)
    webfinger = response.json()
    self.assertEqual(webfinger['subject'].split(':')[1], account_address)
  
  def test_users(self):
    self.load_user()
    response = self.client.get('/users/a')
    
if __name__ == '__main__':
  unittest.main()
