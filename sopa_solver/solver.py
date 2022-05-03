from typing import Iterable, List

from sopa_solver.sopa import Sopa

movement_x = [0, 1, 1, 1, 0, -1, -1, -1]
movement_y = [-1, -1, 0, 1, 1, 1, 0, -1]


class SopaSolver:
    """ Sopa de letras finder

    """

    def __init__(self):
        self.sopa_word = None

    def set_sopa(self, sopa: Sopa) -> None:
        """

        Args:
            sopa: Letter Soup instance problem

        Returns: None

        """
        self.sopa_word = sopa

    def find_word(self, word: str) -> bool:
        """ Find word in a current soup instance

        Args:
            word: word to find

        Returns: True if word in soup map

        """
        row = 0

        for line in self.sopa_word.matrix:
            start_col_idxs = find_char(word[0], line)
            if len(start_col_idxs) > 0:
                for i in start_col_idxs:
                    if search(word, 0, row, i, self.sopa_word):
                        return True
            row += 1
        return False

    def find_words(self, word_list: List[str]) -> list:
        """

        Args:
            word_list: list to find

        Returns: list with boolean result values

        """
        return [self.find_word(word) for word in word_list]


def find_char(ch: str, line) -> list:
    """ get where the char is in list

    Args:
        ch: char to find
        line: Iterable to search in

    Returns: Indexes where char was found

    """
    r = []
    for i, l in enumerate(line):
        if ch == l:
            r.append(i)
    return r


def get_match_index(word, line) -> Iterable:
    matches = []
    for i, w in enumerate(word):
        for l in line:
            if w == l:
                matches.append(i)
    return matches


def search(word, index, row, col, soup_map: Sopa) -> bool:
    """ Perform search over all de soup map

    Args:
        word: word to sear
        index: current word index to start
        row: Row Letter soup to start
        col: Col Letter soup to start
        soup_map: Letter soup

    Returns: If word ins in lettter soup.

    """
    if index == len(word) - 1:
        return True

    for m in range(len(movement_x)):
        new_x = col + movement_x[m]
        new_y = row + movement_y[m]
        if is_valid(new_x, new_y, word[index + 1], soup_map):
            if search(word, index + 1, new_y, new_x, soup_map):
                return True
    return False


def is_valid(x, y, ch, soup_map: Sopa) -> bool:
    """

    Args:
        x: col
        y: row
        ch: character to find
        soup_map: Soop map where to find

    Returns:

    """
    if x < 0 or x >= soup_map.width:
        return False
    if y < 0 or y >= soup_map.height:
        return False
    if ch == soup_map.get_char(y, x):
        return True
    return False
