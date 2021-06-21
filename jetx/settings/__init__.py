from .base import *
from .test import *
try:
    from .local_settings import *
except ImportError:
    pass
