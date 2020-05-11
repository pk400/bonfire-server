import abc


class JWT(abc.ABC):
  '''Interface for encoding and decoding JSON Web Tokens.'''

  def encode(self, data):
    '''Encodes data to a JWT.

    Args:
      data (Object): The data to encode.

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
      Object: The decoded data.
    '''
    raise NotImplementedError()
