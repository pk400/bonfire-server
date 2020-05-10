from starlette import status
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Route

from server.services.accounts.server import Server


class HttpServer:
  def __init__(self, server):
    self._server = server
    self._app = Starlette(routes=[
      Route('/create_account', self._on_create_account, name='create_account'),
      Route('/login', self._on_login, name='login'),
      Route('/logout', self._on_logout, name='logout')
    ])

  @property
  def app(self):
    return self._app

  async def _on_create_account(self, request):
    params = await request.json()
    await self._server.create_account(request.state.session,
      params['email_address'], params['password'], params['confirm_password'])
    return Response(status_code=status.HTTP_201_CREATED)

  async def _on_login(self, request):
    params = await request.json()
    await self._server.login(request.state.session, params['email_address'],
      params['password'])
    return Response(status_code=status.HTTP_200_OK)

  async def _on_logout(self, request):
    await self._server.logout(request.state.session)
    return Response(status_code=status.HTTP_200_OK)
