from pathlib import Path
from typing import Optional

from sopa_solver import Sopa


def from_file(sopa_promblem: Path) -> Optional[Sopa]:
    """ Letter Reader from .txt text file

    Args:
        sopa_promblem: filename

    Returns: Sopa Object
    Throws: Not file error
    """

    sopa = Sopa()
    with open(sopa_promblem, encoding="utf8") as f:
        while t := f.readline():
            sopa.matrix.append(t.strip().upper().split(sep=" "))

    sopa.height = len(sopa.matrix)
    sopa.width = len(sopa.matrix[0])
    return sopa


def from_array(matrix: list) -> Sopa:
    """ Converter to Sopa Object

    Args:
        matrix:

    Returns:

    """
    sopa = Sopa()
    sopa.matrix = matrix
    sopa.height = len(matrix)
    sopa.width = len(matrix[0])
    return sopa


def read_to_find(letters):
    letters_list = []
    with open(letters, encoding="utf8") as f:
        while t := f.readline():
            letters_list.append(t.strip().upper())
    return letters_list
