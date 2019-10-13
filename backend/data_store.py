import abc

from post import Post

class DataStore:
  @abc.abstractmethod
  async def store_post(self, post):
    pass

  @abc.abstractmethod
  async def load_post(self, post_id):
    pass

  @abc.abstractmethod
  async def store_image_file(self, image_id, image_file):
    pass

  @abc.abstractmethod
  async def load_image(self, image_id):
    pass

class LocalDataStore(DataStore):
  def __init__(self):
    self._posts = []
    self._images = {}

  async def store_post(self, post):
    self._posts.append(post)

  async def load_all_posts(self):
    return self._posts

  async def load_post(self, post_id):
    for post in self._posts:
      if post.post_id == post_id:
        return post
    return Post(None, None, None)

  async def store_image_file(self, image_id, image_file):
    self._images[image_id] = image_file

  async def load_image(self, image_id):
    return self._images[image_id]
