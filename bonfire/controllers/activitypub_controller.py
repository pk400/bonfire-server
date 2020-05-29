from starlette.applications import Starlette
from starlette.routing import Route

from bonfire.models.actor import Actor


class ActivityPubController:
  def __init__(self, server):
    self._server = server
    routes = [
      Route('/actor', self._actor, methods=['GET'])
    ]
    self._asgi_app = Starlette(routes=routes)

  @property
  def asgi_app(self):
    return self._asgi_app

  async def actor(self, request):
    actor = Actor()
