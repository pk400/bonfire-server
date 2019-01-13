class Account:
  def __init__(self, id, username, password, email_address):
    self._id = id
    self._username = username
    self._password = password
    self._email_address = email_address

  @property
  def id(self):
    return self._id
  
  @property
  def username(self):
    return self._username

  @property
  def password(self):
    return self._password

  @property
  def email_address(self):
    return self._email_address
