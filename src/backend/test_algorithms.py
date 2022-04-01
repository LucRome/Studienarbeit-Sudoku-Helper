import unittest
from algorithms.algorithms import *
from sudoku.base import Field, Sudoku


class TestAlgorithms(unittest.TestCase):



    def test_unique(self):

#sudoku with 1 solution
        grid = []
        grid.append([2, 6, None, None, None, None, None, None, None])
        grid.append([1, None, None, 8, None, None, None, None, None])
        grid.append([None, None, None, 9, 6, 2, None, None, None])
        grid.append([None, None, None, 3, None, None, 7, None, None])
        grid.append([None, None, None, None, 5, None, None, None, 8])
        grid.append([None, None, 2, 7, 4, None, None, 9, None])
        grid.append([4, None, None, None, None, None, None, 2, None])
        grid.append([7, None, 3, None, None, 6, None, None, None])
        grid.append([None, None, None, 3, None, None, None, 8, 1])

        grid2 = []
        grid2.append([None, None, None, 1, 3, 7, None, None, None])
        grid2.append([7, None, None, 5, 9, 6, 1, 3, None])
        grid2.append([None, None, 9, None, 8, None, None, 6, None])
        grid2.append([None, None, 3, None, 2, None, None, None, None])
        grid2.append([5, None, None, 8, None, None, 9, 2, None])
        grid2.append([None, 2, None, None, 1, None, None, None, None])
        grid2.append([None, None, None, None, None, None, None, None, 8])
        grid2.append([8, 7, 4, None, None, None, None, None, None])
        grid2.append([None, 6, 5, 3, 4, 8, None, None, None])
       
        sudoku1: Sudoku = Sudoku(grid2)
        sudoku1.select_candidates()
        algo = Algorithm(sudoku1)
        bol,stri = algo.algorithm_3()
        print('Bool:',bol)
        print('String:',stri)