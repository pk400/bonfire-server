from activitypub.object import Object

class Actor(Object):
  def __init__(self, inbox, outbox, following, followers, liked, streams,
      preferred_username, endpoints, proxy_url, oauth_authorization_endpoint,
      oauth_token_endpoint, provide_client_key, sign_client_key, shared_inbox):
    self._inbox = inbox
    self._outbox = outbox
    self._following = following
    self._followers = followers
    self._liked = liked
    self._streams = streams
    self._preferred_username = preferred_username
    self._endpoints = endpoints
    self._proxy_url = proxy_url
    self._oauth_authorization_endpoint = oauth_authorization_endpoint
    self._oauth_token_endpoint = oauth_token_endpoint
    self._provide_client_key = provide_client_key
    self._sign_client_key = sign_client_key
    self._shared_inbox = shared_inbox
