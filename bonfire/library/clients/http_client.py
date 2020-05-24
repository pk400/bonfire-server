import aiohttp

from bonfire.library.types import ServiceType
from bonfire.library.utils import run_in_loop


class HttpClient(ServiceType):
  def __init__(self, site_url):
    self._site_url = site_url
    self._session = None
    self._is_open = False

  def startup(self):
    self._session = run_in_loop(aiohttp.ClientSession())

  def shutdown(self):
    run_in_loop(self._session.close())

  async def get(self, endpoint, data={}):
    return await self._session.get(self._build_url(endpoint), data=data)

  async def post(self, endpoint, json={}):
    return await self._session.post(self._build_url(endpoint), json=json)

  def _build_url(self, endpoint):
    return f'{self._site_url}{endpoint}'
