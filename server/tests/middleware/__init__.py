import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),
  '../..')))

from tests.middleware.session_middleware_tester import SessionMiddlewareTester

__all__ = ['SessionMiddlewareTester']
