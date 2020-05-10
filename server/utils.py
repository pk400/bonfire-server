import asyncio

from exceptions import ServiceNotOpenException, ExceptionCodes

def require_open(inner):
  def wrapper(self, *args, **kwargs):
    if not self._is_open:
      raise ServiceNotOpenException(f'{self.__class__.__name__} is not open.',
        ExceptionCodes.NOT_OPEN)
    return inner(self, *args, **kwargs)
  return wrapper

def run_in_loop(coro):
  return asyncio.get_event_loop().run_until_complete(coro)
