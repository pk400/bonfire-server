class Account:
  def __init__(self, id, email_address):
    self._id = id
    self._email_address = email_address

  @property
  def id(self):
    return self._id

  @property
  def email_address(self):
    return self._email_address

Account.NONE = Account(-1, '')
