import unittest
from algorithms.algorithms import *
from .utils import intersection_of_units, has_removed_candidates
from sudoku.base import Field, Sudoku

# TODO

class UtilTest(unittest.TestCase):
    
    def test_intersection_of_units(self):
        # Block 2 and Row 2
        expected = [(2, 6), (2, 7), (2, 8)]
        given = intersection_of_units(UnitType.BLOCK, 2, UnitType.ROW, 2)
        self.assertListEqual(expected, given)
        # Block 0 and Column 1
        expected = [(0, 1), (1, 1), (2, 1)]
        given = intersection_of_units(UnitType.BLOCK, 0, UnitType.COLUMN, 1)
        self.assertListEqual(expected, given)
        # Row 0 and Column 0
        expected = [(0, 0)]
        given = intersection_of_units(UnitType.ROW, 0, UnitType.COLUMN, 0)
        self.assertListEqual(expected, given)

    def test_removed(self):
        a = {
            1: [],
            2: []
        }
        self.assertFalse(has_removed_candidates(a))

        b = {
            1: [1],
            2: []
        }
        self.assertTrue(has_removed_candidates(b))

        c = {}
        self.assertFalse(has_removed_candidates(c))