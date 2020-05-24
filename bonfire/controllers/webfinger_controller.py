from starlette import status
from starlette.applications import Starlette
from starlette.responses import JSONResponse, Response
from starlette.routing import Route

from bonfire.models.jrd import JRD


class WebFingerController:
  def __init__(self, accounts_client):
    self._accounts_client = accounts_client
    self._supported_uris = {
      'acct': self.acct_handler
    }
    self._supported_media_types = {
      'application/jrd+json': JRD
    }
    routes = [
      Route('/webfinger', self.webfinger, methods=['GET'])
    ]
    self._asgi_app = Starlette(routes=routes)

  @property
  def asgi_app(self):
    return self._asgi_app

  async def webfinger(self, request):
    query_params = request.query_params
    if 'resource' not in query_params:
      return Response(status_code=status.HTTP_400_BAD_REQUEST)
    resource = query_params['resource']
    uri, value = resource.split(':')
    if uri not in self._supported_uris:
      return Response(status_code=status.HTTP_404_NOT_FOUND)
    resource_handler = self._supported_uris[uri]
    rels = []
    if 'rel' in query_params:
      for x in query_params.getlist('rel'):
        rels.append(('rel', x))
    data = await resource_handler(value, rels)
    return JSONResponse(data.to_json())

  async def acct_handler(self, email_address, rels):
    account = \
      await self._accounts_client.load_account_by_email_address(email_address)
    jrd = JRD(account.email_address)
    return jrd
