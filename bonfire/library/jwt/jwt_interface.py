import abc


class JWTInterface(abc.ABC):
  '''Interface for encoding and decoding JSON Web Tokens.'''

  def encode(self, json_data):
    '''Encodes data to a JWT.

    Args:
      json_data (dict): The payload to encode.

    Raises:
      jwt.JWTEncodeError: Failed to encode the data.

    Returns:
      str: The encoded JWT string.
    '''
    raise NotImplementedError()

  def decode(self, token):
    '''Decodes data from a JWT.

    Args:
      token (str): The encoded JWT string.

    Raises:
      jwt.InvalidTokenError: Token is not a valid JWT.

    Returns:
      dict:
    '''
    raise NotImplementedError()
