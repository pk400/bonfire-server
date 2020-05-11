from library.generators.sequence_generator import SequenceGenerator
from library.jwt import ErrorCode, InvalidTokenError
from library.serializer import Serializer


# TODO: Rework JWT classes. TestJWT should not have to know to_type in from_json.



class TestJWT:
  '''JWT implementation for testing.'''

  def __init__(self):
    '''Constructs a TestJWT.'''
    self._token_to_data = {}
    self._token = SequenceGenerator()

  def encode(self, data):
    token_key = str(self._token.generate())
    payload = Serializer.to_json(data)
    self._token_to_data[token_key] = payload
    return token_key

  def decode(self, token):
    if token not in self._token_to_data:
      raise InvalidTokenError(f'Failed to decode token: {token}',
        ErrorCode.INVALID_TOKEN)
    payload = self._token_to_data[token]
    return Serializer.from_json(payload, Session)
