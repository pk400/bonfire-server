import abc


class PasswordHasher:
  '''Hashing password interface.'''

  @abc.abstractmethod
  def hash_password(self, plaintext_password: str):
    '''Hash a password.

    Args:
      plaintext_password (str): The password to hash as a plain-text string.

    Returns:
      bytes: The resulting hashed password.
    '''
    raise NotImplementedError()

  @abc.abstractmethod
  def check_password(self, plaintext_password: str, hashed_password: bytes):
    '''Checks a plain-text password against a hashed password.

    Args:
      plaintext_password (str): The password as a plain-text string.
      hashed_password (bytes): The hashed password to compare against.

    Returns:
      bool: True if the password matches the hashed password, False otherwise.
    '''
    raise NotImplementedError()
