class Account:
  def __init__(self, username, email_address, password):
    self._username = username
    self._email_address = email_address
    self._password = password
    self._account_id = None
    self._webfinger = None
    self._actor = None
  
  @property
  def username(self):
    return self._username

  @property
  def email_address(self):
    return self._email_address

  @property
  def password(self):
    return self._password

  @property
  def account_id(self):
    return self._account_id

  @property
  def webfinger(self):
    return self._webfinger
  
  @property
  def actor(self):
    return self._actor

  @username.setter
  def username(self, username):
    self._username = username

  @email_address.setter
  def email_address(self, email_address):
    self._email_address = email_address
  
  @account_id.setter
  def account_id(self, id):
    self._account_id = id
  
  @password.setter
  def password(self, password):
    self._password = password
  
  @webfinger.setter
  def webfinger(self, webfinger):
    self._webfinger = webfinger

  @actor.setter
  def actor(self, actor):
    self._actor = actor
