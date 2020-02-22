class Session:
  def __init__(self):
    self._id = None

  @property
  def id(self):
    return self._id

  def set_credentials(self, id):
    self._id = id

  def reset_credentials(self):
    self._id = None
