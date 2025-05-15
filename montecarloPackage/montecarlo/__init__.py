"""This file will turn a directory into a python package"""

# Add imports here
from .functions import *
from .bitString import BitString
from .isingHamiltonian import IsingHamiltonian
from ._version import __version__

__all__ = [
    "IsingHamiltonian",
    "BitString",
    "__version__"
]