import enum

class ExceptionCodes(enum.Enum):
  NOT_OPEN = 0

class BonfireException(Exception):
  def __init__(self, message, code):
    self._message = message
    self._code = code

  @property
  def message(self):
    return self._message

  @property
  def code(self):
    return self._code

class BadCredentialsException(BonfireException):
  pass

class ServiceNotOpenException(BonfireException):
  pass
