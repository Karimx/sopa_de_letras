import pytest

from sopa_solver import SopaSolver, loader


ciertas = [
    "COW",
    "TIBURÓN",
    "LEOPARDO",
    "PUMA",
    "COCODRILO",
    "LEÓN",
    "DELFÍN",
    "TIGRE",
    "ÁGUILA",
    "LOBO",
    "GUEPARDO",
    "PUP",
]
falsas = ["ANGUILA", "PARROT", "TIBURON", "BUFALO", "MOUSE"]


sopa = [
    ["J", "V", "Ó", "R", "U", "B", "I", "0", "F", "N", "N", "Y", "A", "T", "F"],
    ["C", "L", "V", "Ó", "U", "M", "T", "L", "Y", "L", "B", "H", "D", "W", "J"],
    ["H", "U", "V", "N", "H", "O", "C", "A", "Y", "O", "B", "D", "Y", "I", "G"],
    ["C", "O", "W", "T", "R", "D", "B", "Z", "T", "U", "U", "P", "C", "E", "U"],
    ["E", "X", "A", "C", "A", "G", "H", "R", "G", "F", "P", "E", "O", "H", "E"],
    ["Q", "X", "Y", "V", "P", "L", "I", "N", "E", "Y", "X", "V", "C", "W", "P"],
    ["O", "B", "O", "M", "O", "H", "K", "Ó", "E", "H", "M", "H", "O", "M", "A"],
    ["J", "X", "L", "P", "E", "T", "D", "E", "Z", "T", "T", "F", "D", "G", "R"],
    ["D", "E", "T", "N", "L", "W", "W", "L", "S", "A", "I", "G", "R", "W", "D"],
    ["I", "M", "X", "F", "M", "A", "J", "N", "L", "Y", "G", "B", "I", "O", "O"],
    ["C", "C", "P", "O", "I", "U", "Y", "I", "Í", "B", "R", "J", "L", "G", "K"],
    ["O", "R", "Z", "A", "W", "Z", "U", "T", "I", "F", "E", "L", "O", "T", "G"],
    ["Q", "A", "M", "U", "P", "G", "D", "O", "R", "K", "L", "C", "I", "V", "N"],
    ["S", "N", "K", "N", "Á", "Q", "P", "G", "C", "X", "H", "E", "J", "D", "F"],
    ["Z", "S", "P", "F", "M", "L", "P", "S", "S", "Z", "T", "K", "D", "L", "G"],
]


def sopa_solver():
    sopa_solver = SopaSolver()
    sopa_solver.set_sopa(loader.from_array(sopa))
    return sopa_solver

@pytest.param
def test_correct(sopa_solver):

    sopa_solver = SopaSolver()
    sopa_solver.set_sopa(loader.from_array(sopa))
    for c in ciertas:
        assert sopa_solver.find_word(c) == True


def test_incorrect():
    sopa_solver = SopaSolver()
    sopa_solver.set_sopa(loader.from_array(sopa))
    for f in falsas:
        assert sopa_solver.find_word(f) == False
