import abc


class Client(abc.ABC):
  @abc.abstractmethod
  def create_account(self, email_address, password):
    raise NotImplementedError()

  def set_credentials(self, email_address, password):
    raise NotImplementedError()

  def open(self):
    raise NotImplementedError()

  def close(self):
    raise NotImplementedError()
