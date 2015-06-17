
from sladoku.model.norvig import Puzzle

import unittest

class PuzzleTest(unittest.TestCase):

    def test_puzzle_definition(self):
        "Test the definition of the puzzle at the class level"
        self.assertEqual(len(Puzzle.squares),81)
        self.assertEqual(len(Puzzle.unitlist),27)

        self.assertTrue(all(len(Puzzle.units[s]) == 3) for s in Puzzle.squares)
        self.assertTrue(all(len(Puzzle.peers[s]) == 20) for s in Puzzle.squares)

        self.assertEqual(Puzzle.units['C2'],
                         [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                          ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                          ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']])
        self.assertEqual(Puzzle.peers['C2'],
                         set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                              'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                              'A1', 'A3', 'B1', 'B3']))

    def test_puzzle_instance(self):
        "Test the definition of the puzzle for a specific instance"
        puzzle = Puzzle()

        self.assertEqual(len(puzzle.squares),81)
        self.assertEqual(len(puzzle.unitlist),27)

        self.assertTrue(all(len(puzzle.units[s]) == 3) for s in puzzle.squares)
        self.assertTrue(all(len(puzzle.peers[s]) == 20) for s in puzzle.squares)

        self.assertEqual(puzzle.units['C2'],
                         [['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
                          ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
                          ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']])
        self.assertEqual(puzzle.peers['C2'],
                         set(['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
                              'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                              'A1', 'A3', 'B1', 'B3']))
        

    def test_parse_singleline(self):
        grid = Puzzle.parse("4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......")
        self.assertEqual(len(grid),81)
        self.assertEqual(grid['A1'],'4')
        self.assertEqual(grid['A2'],'.')
        self.assertEqual(grid['B2'],'3')
        self.assertEqual(grid['G8'],'7')

    def test_parse_all_digits(self):
        str = """
        400000805
        030000000
        000700000
        020000060
        000080400
        000010000
        000603070
        500200000
        104000000"""
        grid = Puzzle.parse(str)
        self.assertEqual(len(grid),81)
        self.assertEqual(grid['A1'],'4')
        self.assertEqual(grid['A2'],'.')
        self.assertEqual(grid['B2'],'3')
        self.assertEqual(grid['G8'],'7')

    def test_parse_formatted(self):
        str = """
        4 . . |. . . |8 . 5 
        . 3 . |. . . |. . . 
        . . . |7 . . |. . . 
        ------+------+------
        . 2 . |. . . |. 6 . 
        . . . |. 8 . |4 . . 
        . . . |. 1 . |. . . 
        ------+------+------
        . . . |6 . 3 |. 7 . 
        5 . . |2 . . |. . . 
        1 . 4 |. . . |. . . 
        """
        grid = Puzzle.parse(str)
        self.assertEqual(len(grid),81)
        self.assertEqual(grid['A1'],'4')
        self.assertEqual(grid['A2'],'.')
        self.assertEqual(grid['B2'],'3')
        self.assertEqual(grid['G8'],'7')
        
