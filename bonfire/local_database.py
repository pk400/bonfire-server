from uuid import uuid4

class LocalDataBase:
  def __init__(self, url):
    self.database = {}
    self.url = url
    self.host = self.url.split('://')[1]

  def store_account(self, account):
    account.account_id = uuid4()
    user_address = '@'.join([account.username, self.host])
    account.webfinger = {
      'subject': ':'.join(['acct', user_address]),
      'links': [
        {
          'rel': 'self',
          'type': 'application/activity+json',
          'href': '/'.join([self.url, 'users', account.username])
        }
      ]
    }
    account.actor = {
      '@context': [
        'https://www.w3.org/ns/activitystreams',
        'https://w3id.org/security/v1'
      ],
      'id': '/'.join([self.url, 'users', account.username]),
      'type': 'Person',
      'preferredUsername': account.username,
      'inbox': '/'.join([self.url, 'inbox'])
    }
    self.database[account.username] = account

  def load_account(self, username):
    if username in self.database:
      return self.database[username]
    return None
