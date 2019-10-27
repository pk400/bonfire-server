class Account:
  def __init__(self, account_id, username, email_address, password):
    self._account_id = account_id
    self._username = username
    self._email_address = email_address
    self._password = password

  @property
  def account_id(self):
    return self._account_id

  @property
  def username(self):
    return self._username

  @property
  def email_address(self):
    return self._email_address

  @property
  def password(self):
    return self._password

Account.NONE = Account(-1, '', '', '')
