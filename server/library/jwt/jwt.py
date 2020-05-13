import jwt

from library.jwt.jwt_interface import JWTInterface


class JWT(JWTInterface):
  def __init__(self, secret, algorithms=['HS256']):
    self._secret = secret
    self._algorithms = algorithms

  def encode(self, json_data, algorithm='HS256'):
    return jwt.encode(json_data, self._secret, algorithm=algorithm)

  def decode(self, token):
    return jwt.decode(token, self._secret, algorithms=self._algorithms)
