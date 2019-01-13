from starlette.applications import Starlette
from starlette.responses import JSONResponse

from server.accounts import AccountsError

def AccountsHttpServer(server):
  app = Starlette()

  @app.exception_handler(AccountsError)
  def accounts_error_handler(request, exc):
    return JSONResponse(str(exc), status_code=400)

  @app.route('/create_account', methods=['POST'])
  async def create_account(request):
    params = require_valid_params(await request.json(),
      ['username', 'password', 'email_address'])
    account = server.create_account(params)
    return JSONResponse(account.username)

  def require_valid_params(params, valid_params):
    if not all(key in params for key in valid_params):
      raise AccountsError('Invalid parameters', 0)
    return params

  return app
