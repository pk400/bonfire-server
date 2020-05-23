from starlette.endpoints import HTTPEndpoint
from starlette.responses import Response
from starlette.routing import Router

'''
/.well-known/webfinger?
  resource=acct%3Abob%40example.com&
  rel=http%3A%2F%2Fwebfinger.example%2Frel%2Fprofile-page&
  rel=http%3A%2F%2Fwebfinger.example%2Frel%2Fbusinesscard

- resource
- rel
'''

WebFingerRouter = Router()

@WebFingerRouter.route('/.well-known/webfinger')
class WebFingerEndpoint(HTTPEndpoint):
  async def get(self, request):
    params = request.query_params['resource']
    print(params)
    return Response()


# -----
# TESTS

from starlette.applications import Starlette
from starlette.testclient import TestClient

app = Starlette()
app.add_route('/test', WebFingerEndpoint)

if __name__ == '__main__':
  with TestClient(app) as client:
    client.get('/test', params={'resource': 'world'})
