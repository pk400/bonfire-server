from server.types.password_hasher.password_hasher import PasswordHasher


class BcryptPasswordHasher(PasswordHasher):
  def hash_password(self, plaintext_password: str):
    pass

  def check_password(self, plaintext_password: str, hashed_password: bytes):
    pass
