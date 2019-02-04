class Account:
  def __init__(self, username, password):
    self._username = username
    self._password = password
    self._account_id = None
    self._webfinger = None
    self._actor = None
  
  @property
  def username(self):
    return self._username

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
