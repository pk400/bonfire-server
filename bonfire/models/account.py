class Account:
  def __init__(self, id, email_address, username):
    self._id = id
    self._email_address = email_address
    self._username = username

  @property
  def id(self):
    return self._id

  @property
  def email_address(self):
    return self._email_address

  @property
  def username(self):
    return self._username


Account.NONE = Account(-1, '', '')
