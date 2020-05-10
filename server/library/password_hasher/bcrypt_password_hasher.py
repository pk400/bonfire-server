import bcrypt

from library.password_hasher.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
  '''Password hasher implementation using Bcrypt.'''

  def __init__(self):
    '''Constructs a BcryptPasswordHasher.'''
    self._salt = bcrypt.gensalt()
    self._encoding = 'utf-8'

  def hash_password(self, plaintext_password: str):
    return bcrypt.hashpw(plaintext_password.encode(self._encoding), self._salt)

  def check_password(self, plaintext_password: str, hashed_password: bytes):
    return bcrypt.checkpw(plaintext_password.decode(self._encoding),
      hashed_password)
