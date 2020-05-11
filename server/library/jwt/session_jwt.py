import jwt

from library.jwt import JWT
from library.serializer import Serializer


class SessionJWT(JWT):
  '''JWT implementation for encoding and decoding sessions.'''

  def __init__(self, secret, algorithm):
    '''Constructs a SessionJWT.

    Args:
      secret (str): JWT secret.
      algorithm (str): Algorithm to serialize JWT.
    '''
    self._secret = secret
    self._algorithm = 'HS256'
    self._jwt = jwt

  def encode(self, data):
    payload = Serializer.to_json(data)
    token = self._jwt.encode(payload, self._secret, algorithm=self._algorithm)
    return token

  def decode(self, token):
    payload = self._jwt.decode(token, self._secret,
      algorithms=[self._algorithm])
    return Serializer.from_json(payload)
