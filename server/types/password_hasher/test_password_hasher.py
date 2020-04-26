from server.types.password_hasher.password_hasher import PasswordHasher


class TestPasswordHasher(PasswordHasher):
  '''Simple password hasher for testing.'''

  def __init__(self):
    '''Constructs a SimplePasswordHasher.'''
    self._seq_id_to_password = {}
    self._seq_id = 0

  def hash_password(self, plaintext_password: str):
    seq_id = self._seq_id
    self._seq_id_to_password[seq_id] = plaintext_password
    self._seq_id += 1
    return seq_id


  def check_password(self, plaintext_password: str, hashed_password: bytes):
    pass
