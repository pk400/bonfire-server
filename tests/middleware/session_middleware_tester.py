import unittest

from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from starlette.testclient import TestClient

from bonfire.library.jwt import TestJWT
from bonfire.library.middleware import SessionMiddleware
from bonfire.library.types import MutableSession


class MockSession(MutableSession):
  def __init__(self, value):
    super().__init()
    self._value = value

  @property
  def value(self):
    return self._value

  def set_value(self, value):
    self._value = value


class SessionMiddlewareTester(unittest.TestCase):
  def setUp(self):
    self.jwt = TestJWT()

  def test_session_cookie_not_set(self):
    async def mock_route(request):
      return Response(status_code=200)

    cookie_name = 'x'
    app = Starlette(routes=[Route('/', mock_route)],
      middleware=[Middleware(SessionMiddleware, cookie_name=cookie_name,
        jwt=self.jwt)])
    with TestClient(app) as client:
      response = client.get('/')
      self.assertNotIn(cookie_name, response.cookies)
      self.assertNotIn(cookie_name, client.cookies)

  def test_session_cookie_is_set(self):
    async def mock_route(request):
      request.session.set_credentials(99)
      return Response(status_code=200)

    cookie_name = 'x'
    app = Starlette(routes=[Route('/', mock_route)],
      middleware=[Middleware(SessionMiddleware, cookie_name=cookie_name,
        jwt=self.jwt)])
    with TestClient(app) as client:
      response = client.get('/')
      self.assertIn(cookie_name, response.cookies)
      self.assertIn(cookie_name, client.cookies)

  def test_session_persists_across_requests(self):
    async def r1(request):
      request.session.set_credentials(99)
      return Response(status_code=200)

    async def r2(request):
      return JSONResponse({'id': request.session.id}, status_code=200)

    cookie_name = 'x'
    app = Starlette(routes=[Route('/r1', r1), Route('/r2', r2)],
      middleware=[Middleware(SessionMiddleware, cookie_name=cookie_name,
        jwt=self.jwt)])
    with TestClient(app) as client:
      response = client.get('/r1')
      self.assertIn(cookie_name, response.cookies)
      self.assertIn(cookie_name, client.cookies)
      response = client.get('/r2')
      session_id = response.json()['id']
      self.assertEqual(session_id, 99)


if __name__ == '__main__':
  unittest.main()
