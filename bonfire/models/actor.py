from bonfire.models.object import Object


class Actor(Object):
  def __init__(self, inbox, outbox):
    self._inbox = inbox
    self._outbox = outbox

  following = None
  followers = None
  liked = None
  streams = None
  preferred_username = None
  endpoints = None
