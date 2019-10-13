import abc

from interfaces.data_store import DataStore

class DataStore(DataStore):
  @abc.abstractmethod
  async def store_post(self, post):
    raise NotImplementedError()

  @abc.abstractmethod
  async def load_all_posts(self):
    raise NotImplementedError()

  @abc.abstractmethod
  async def load_post(self, post_id):
    raise NotImplementedError()

  @abc.abstractmethod
  async def search_posts(self, filter):
    raise NotImplementedError()

  @abc.abstractmethod
  async def store_image_file(self, image_id, image_file):
    raise NotImplementedError()

  @abc.abstractmethod
  async def load_image(self, image_id):
    raise NotImplementedError()
