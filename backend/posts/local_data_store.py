from posts.data_store import DataStore
from posts.post import EmptyPost

class LocalDataStore(DataStore):
  def __init__(self):
    self._posts = {}
    self._images = {}

  def open(self):
    self._is_open = True

  def close(self):
    self._is_open = False

  async def store_post(self, post):
    self._posts[post.post_id] = post

  async def load_all_posts(self):
    return self._posts

  async def load_post(self, post_id):
    return self._posts.get(post_id, EmptyPost())

  async def search_posts(self, filter):
    posts = []
    for post in self._posts.values():
      if post.post_id >= filter['range'][0] and post.post_id <= filter['range'][1]:
        posts.append(post)
      if len(posts) == filter['limit']:
        break
    return posts

  async def store_image_file(self, image_id, image_file):
    self._images[image_id] = image_file

  async def load_image(self, image_id):
    return self._images[image_id]
