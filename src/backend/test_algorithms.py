import unittest
from algorithms.algorithms import *
from sudoku.base import Field, Sudoku


class TestAlgorithms(unittest.TestCase):



    def test_unique(self):

#sudoku with 1 solution
        grid = []
        grid.append([None, 7, None, None, None, None, None, 1, 2])
        grid.append([None, None, None, None, 3, 5, None, None, None])
        grid.append([None, None, None, 6, None, None, None, 7, None])
        grid.append([7, None, 8, None, None, None, 3, None, None])
        grid.append([None, None, None, 4, None, None, 8, None, None])
        grid.append([1, None, None, None, None, None, None, None, None])
        grid.append([None, None, None, 1, 2, None, None, None, None])
        grid.append([None, 8, None, None, None, None, None, 4, None])
        grid.append([None, 5, None, None, None, None, 6, None, 8])
       
        sudoku1: Sudoku = Sudoku(grid)
        sudoku1.select_candidates()
        algo = Algorithm(sudoku1)