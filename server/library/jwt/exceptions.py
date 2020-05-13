import enum

from library import exceptions


class ErrorCode(enum.Enum):
  INVALID_TOKEN = enum.auto()


class JWTBaseError(exceptions.BonfireException):
  pass


class JWTEncodeError(JWTBaseError):
  pass


class JWTDecodeError(JWTBaseError):
  pass


class InvalidTokenError(JWTDecodeError):
  pass
