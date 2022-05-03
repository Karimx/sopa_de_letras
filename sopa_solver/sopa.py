class Sopa:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.matrix: list = []

    def matrix_get(self) -> list:
        return self._matrix

    def matrix_setter(self, matrix) -> None:
        self._matrix = matrix

    def get_char(self, x, y) -> str:
        return self.matrix[x][y]
