from uuid import uuid4

class LocalDataBase:
  def __init__(self):
    self.database = {}

  def store_account(self, account):
    account.account_id = uuid4()
    account.webfinger = {
      'subject': ':'.join(['acct', account.email_address]),
      'links': [
        {
          'rel': 'self',
          'type': 'application/activity+json',
          'href': '/'.join(['https://astraea.systems/users', account.username])
        }
      ]
    }
    account.actor = {
      '@context': [
        'https://www.w3.org/ns/activitystreams',
        'https://w3id.org/security/v1'
      ],
      'id': '/'.join(['https://astraea.systems', account.username]),
      'type': 'Person',
      'preferredUsername': account.username,
      'inbox': 'https://astraea.systems/inbox'
    }
    self.database[account.username] = account

  def load_account(self, username):
    if username in self.database:
      return self.database[username]
    return None

  def load_account_by_email(self, email_address):
    for account in self.database.values():
      if account.email_address == email_address:
        return account
    return None
