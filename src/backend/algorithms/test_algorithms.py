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

        grid4 = []
        grid4.append([None, None, None, None, None, None, None, None, None])
        grid4.append([4, None, None, None, 7, None, 6, None, None])
        grid4.append([None, 7, None, 2, None, 4, 3, None, None])
        grid4.append([None, None, None, 9, None, None, None, 8, 4])
        grid4.append([None, 6, None, None, None, None, 5, 9, 2])
        grid4.append([5, 9, None, None, None, None, None, None, None])
        grid4.append([None, 4, None, 8, 2, None, 9, None, 1])
        grid4.append([None, None, None, 1, None, None, None, None, None])
        grid4.append([6, 5, 1, 7, None, None, None, None, None])
                
        grid5 = []
        grid5.append([None, 7, None, None, None, None, 8, None, None])
        grid5.append([None, 2, None, 8, None, None, 9, 5, None])
        grid5.append([None, None, None, None, None, 9, 6, None, 2])
        grid5.append([None, None, None, 3, None, 4, 2, 8, 9])
        grid5.append([None, None, 3, 9, None, None, 1, 6, 4])
        grid5.append([4, None, None, 6, 1, None, 5, None, None])
        grid5.append([None, 4, None, 2, 9, 6, None, 1, 5])
        grid5.append([None, None, None, None, None, None, None, 9, 6])
        grid5.append([None, None, None, 5, 3, None, 4, 2, 8])
       
        grid6 = []
        grid6.append([None, None, None, 7, 4, None, None, None, 8])
        grid6.append([4, 9, 6, None, None, None, None, None, None])
        grid6.append([None, None, None, None, 2, None, None, 4, None])
        grid6.append([None, None, None, None, 5, 7, 6, None, None])
        grid6.append([8, None, None, None, None, None, None, 2, 1])
        grid6.append([None, None, 3, 4, None, None, None, None, None])
        grid6.append([None, None, None, 3, None, None, None, None, None])
        grid6.append([1, 2, 4, None, 7, None, None, 5, None])
        grid6.append([None, None, None, None, None, None, 7, None, None])
        
        #grid4 = []
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
        #grid4.append([None, None, None, None, None, None, None, None, None])
       
        sudoku1: Sudoku = Sudoku(grid6)
        sudoku1.select_candidates()
        algo = Algorithm(sudoku1)
        bol,stri = algo.algorithm_6()
        print('Bool:',bol)
        print('String:',stri)