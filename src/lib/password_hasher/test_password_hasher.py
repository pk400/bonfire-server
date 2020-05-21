from lib.generators import SequenceGenerator
from lib.password_hasher import PasswordHasher


class TestPasswordHasher(PasswordHasher):
  '''Simple password hasher for testing.'''

  def __init__(self):
    '''Constructs a SimplePasswordHasher.'''
    self._sequence_id_to_password = {}
    self._sequence_generator = SequenceGenerator()

  def hash_password(self, plaintext_password: str):
    sequence_id = self._sequence_generator.generate()
    self._sequence_id_to_password[sequence_id] = plaintext_password
    return bytes([sequence_id])

  def check_password(self, plaintext_password: str, hashed_password: bytes):
    sequence_id = int.from_bytes(hashed_password, 'big')
    return self._sequence_id_to_password[sequence_id] == plaintext_password
