from starlette.middleware.base import BaseHTTPMiddleware

from accounts.session import Session
from library.serializer import Serializer

class SessionMiddleware(BaseHTTPMiddleware):
  def __init__(self, app, cookie_name):
    self._app = app
    self._cookie_name = cookie_name

  def __call__(self, request, call_next):
    if self._cookie_name in request.cookies:
      request.state.session = \
        Serializer.from_json(request.cookies[self._cookie_name], Session)
    else:
      request.state.session = Session()
    response = await call_next(request)
    if 'session' in request.state:
      response.set_cookie(self._cookie_name,
        Serializer.to_json(request.state.session))
    return response

