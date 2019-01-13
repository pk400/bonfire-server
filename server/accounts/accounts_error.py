class AccountsError(Exception):
  def __init__(self, message, code=0):
    self._message = message
    self._code = code

  @property
  def message(self):
    return self._message

  @property
  def code(self):
    return self._code
