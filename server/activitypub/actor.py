from server.activitypub.object import Object


class Actor(Object):
  inbox = None
  outbox = None
  following = None
  followers = None
  liked = None
  streams = None
  preferred_username = None
  endpoints = None
