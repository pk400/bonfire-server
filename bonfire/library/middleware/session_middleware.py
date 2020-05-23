from starlette.middleware.base import BaseHTTPMiddleware

from bonfire.library.accounts.session import Session
from bonfire.library.jwt import JWTDecodeError
from bonfire.library.serializer import Serializer


class SessionMiddleware(BaseHTTPMiddleware):
  def __init__(self, app, cookie_name, jwt):
    super().__init__(app)
    self._cookie_name = cookie_name
    self._jwt = jwt

  async def dispatch(self, request, call_next):
    cookie_data = request.cookies.get(self._cookie_name, '')
    try:
      payload = self._jwt.decode(cookie_data)
      session = Serializer.from_json(payload, Session)
    except JWTDecodeError:
      session = Session()
    request.scope['session'] = session
    response = await call_next(request)
    if session.is_modified:
      payload = Serializer.to_json(session)
      token = self._jwt.encode(payload)
      response.set_cookie(self._cookie_name, token)
    return response
