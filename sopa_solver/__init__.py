from enum import Enum

from .loader import from_array, from_file
from .solver import Sopa, SopaSolver

__all__ = [SopaSolver, Sopa, from_array, from_file]
