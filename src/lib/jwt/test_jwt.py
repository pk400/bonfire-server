from lib.generators import SequenceGenerator
from lib.jwt import JWTDecodeError, JWTInterface


class TestJWT(JWTInterface):
  '''JWT implementation for testing.'''

  INVALID_TOKEN = 0

  def __init__(self):
    '''Constructs a TestJWT.'''
    self._token_to_data = {}
    self._token = SequenceGenerator()

  def encode(self, json_data):
    token_key = str(self._token.generate())
    self._token_to_data[token_key] = json_data
    return token_key

  def decode(self, token):
    if token not in self._token_to_data:
      raise JWTDecodeError(f'Failed to decode token: {token}',
        TestJWT.INVALID_TOKEN)
    return self._token_to_data[token]
