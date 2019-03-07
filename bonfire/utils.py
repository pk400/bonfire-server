from functools import wraps

def require_open(inner):
  @wraps(inner)
  def decorator(self, *args, **kwargs):
    if self._is_open is False:
      raise IOError('{} is not open.'.format(self.__class__.__name__))
    return inner(self, *args, **kwargs)
  return decorator
