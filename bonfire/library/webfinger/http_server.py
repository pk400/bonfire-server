from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Mount, Route


# https://mastodon.social/.well-known/webfinger?resource=acct:gargron@mastodon.social

class HttpServer:
  def __init__(self, server):
    self._server = server
    routes = [
      Mount('./well-known', routes=[
        Route('/webfinger', self._on_webfinger)
      ])
    ]
    self._app = Starlette(routes=routes)

  async def _on_webfinger(self, request):
    if request['scheme'] != 'https':
      return Response(status_code=495)
    params = request.query_params
    if 'resource' not in params:
      return Response(status_code=400)
    resource = params['resource']
    type, value = resource.split(':')
    if type != 'acct':
      return Response(status_code=400)
    username, host = value.split('@')
