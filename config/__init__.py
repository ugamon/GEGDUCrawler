from config import routing
from config.routing import Descriptor
import os
__all__ = {
    "Descriptor",
    "routing",
}
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

