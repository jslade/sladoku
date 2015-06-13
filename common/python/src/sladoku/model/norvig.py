"""
This model for sudoku puzzles is based on this essay by Peter Norvig:
http://norvig.com/sudoku.html

Each position in the grid is referenced by <row><column>, row=letter, column=digit,
e.g. A1

Each collection of 9 squares is a unit. A unit can be a row, a column, or a box.

"""

import types


def _cross(A,B):
    "Cross project of elements in A an elements in B"
    return [a+b for a in A for b in B]

_digits = '123456789'
_rows = 'ABCDEFGHI'
_cols = _digits

_squares = _cross(_rows,_cols)

_unitlist = ([_cross(_rows,c) for c in _cols] +
              [_cross(r, _cols) for r in _rows] +
              [_cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])

_units = dict((s, [u for u in _unitlist if s in u]) for s in _squares)
_peers = dict((s, set(sum(_units[s],[]))-set([s])) for s in _squares)


class Puzzle(object):
    digits = _digits
    rows = _rows
    cols = _cols
    squares = _squares
    unitlist = _unitlist
    units = _units
    peers = _peers

    empty = '0.'
    
    def __init__(self,values=None):
        # Initially populate each square with all possible digits,
        # which actually means a "blank" puzzle
        self.values = dict((s, self.digits) for s in self.squares)
        self.invalid = []

        if values:
            self.assign_multi(values)

    def is_legal(self):
        return len(self.invalid) == 0

    def assign_multi(self,new_values):
        """
        Assign all the values in the new_values.
        The new_values can be a dict of {s: values} for s in squares,
        or it can be a string representation of the grid that is parsed
        via Puzzle.parse()
        """

        if type(grid) == types.StrType:
            grid = self.parse(grid)

        for s in sorted(grid.keys()):
            d = grid[s]
            self.assign(s,d)

        return self.is_legal()

    @staticmethod
    def parse(grid):
        """ Parse a string representation, made up of 81 meaningful characters, ignoring
            spaces and any extra formatting characters. """
        def norm(c):
            if c in Puzzle.digits: return c
            if c in Puzzle.empty: return '.'
            return None
        
        chars = [c for c in map(lambda c: norm(c),grid) if c is not None]
        assert len(chars) == 81 # TODO: raise an illegal argument exception instead
        return dict(zip(Puzzle.squares, chars))
                
