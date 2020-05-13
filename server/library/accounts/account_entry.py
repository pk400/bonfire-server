from library.accounts.account import Account


class AccountEntry:
  def __init__(self, account, password):
    self._account = account
    self._password = password

  @property
  def account(self):
    return self._account

  @property
  def password(self):
    return self._password


AccountEntry.NONE = AccountEntry(Account.NONE, b'')
