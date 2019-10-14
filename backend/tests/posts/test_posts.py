import asyncio
import unittest

from starlette.testclient import TestClient

from posts.api import PostsAPI
from posts.local_data_store import LocalDataStore
from posts.post import EmptyPost, Post
from posts.routes import app

class TestPosts(unittest.TestCase):
  def test_load_1_post(self):
    data_store = LocalDataStore()
    data_store.open()
    posts = {0: Post(0, 'a', 0, 'a')}
    data_store._posts = posts
    app.state.api = PostsAPI(data_store)
    with TestClient(app) as client:
      response = client.get('/posts/0')
      self.assertEqual(response.status_code, 200)
      self.assertDictEqual(response.json(), posts[0].to_json())
      response = client.get('/posts/1')
      self.assertEqual(response.status_code, 200)
      self.assertDictEqual(response.json(), EmptyPost().to_json())
      response = client.get('/posts/a')
      self.assertEqual(response.status_code, 400)

  def test_load_posts_range(self):
    data_store = LocalDataStore()
    data_store.open()
    posts = {
      0: Post(0, 'a', 0, 'a'),
      1: Post(1, 'b', 1, 'b'),
      2: Post(2, 'c', 2, 'c')
    }
    data_store._posts = posts
    app.state.api = PostsAPI(data_store)
    with TestClient(app) as client:
      response = client.get('/posts?from=0&to=1&limit=2')
      self.assertListEqual(response.json(),
        [post.to_json() for post in [posts[0], posts[1]]])

if __name__ == '__main__':
  unittest.main()
