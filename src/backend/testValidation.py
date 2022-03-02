import unittest
from validation.validation import *
from sudoku.base import Field, Sudoku


class TestValidateSudoku(unittest.TestCase):




    def test_unique(self):

#sudoku with 1 solution
        grid = []
        grid.append([0, 0, 0, 0, 0, 0, 0, 1, 2])
        grid.append([0, 0, 0, 0, 3, 5, 0, 0, 0])
        grid.append([0, 0, 0, 6, 0, 0, 0, 7, 0])
        grid.append([7, 0, 0, 0, 0, 0, 3, 0, 0])
        grid.append([0, 0, 0, 4, 0, 0, 8, 0, 0])
        grid.append([1, 0, 0, 0, 0, 0, 0, 0, 0])
        grid.append([0, 0, 0, 1, 2, 0, 0, 0, 0])
        grid.append([0, 8, 0, 0, 0, 0, 0, 4, 0])
        grid.append([0, 5, 0, 0, 0, 0, 6, 0, 0])

#sudoku with 2 solutions
        grid2 = []
        grid2.append([9, 0, 6, 0, 7, 0, 4, 0, 3])
        grid2.append([0, 0, 0, 4, 0, 0, 2, 0, 0])
        grid2.append([0, 7, 0, 0, 2, 3, 0, 1, 0])
        grid2.append([5, 0, 0, 0, 0, 0, 1, 0, 0])
        grid2.append([0, 4, 0, 2, 0, 8, 0, 6, 0])
        grid2.append([0, 0, 3, 0, 0, 0, 0, 0, 5])
        grid2.append([0, 3, 0, 7, 0, 0, 0, 5, 0])
        grid2.append([0, 0, 7, 0, 0, 5, 0, 0, 0])
        grid2.append([4, 0, 5, 0, 1, 0, 7, 0, 8])


#sudoku with > 20000 solutions
        grid3 = []
        grid3.append([0, 0, 0, 0, 0, 0, 0, 1, 2])
        grid3.append([0, 0, 0, 0, 3, 5, 0, 0, 0])
        grid3.append([0, 0, 0, 6, 0, 0, 0, 7, 0])
        grid3.append([7, 0, 0, 0, 0, 0, 3, 0, 0])
        grid3.append([0, 0, 0, 4, 0, 8, 0, 0, 0])
        grid3.append([1, 0, 0, 0, 0, 0, 0, 0, 0])
        grid3.append([0, 0, 0, 1, 2, 0, 0, 0, 0])
        grid3.append([0, 8, 0, 0, 0, 0, 0, 4, 0])
        grid3.append([0, 5, 0, 0, 0, 0, 6, 0, 0])
        
        

        sudoku1: Sudoku = Sudoku(grid)
        counter = validateSudoku(sudoku1,0)
        self.assertAlmostEqual(counter,1)
        print(counter)

        sudoku2: Sudoku = Sudoku(grid)
        counter = validateSudoku(sudoku2,0)
        self.assertAlmostEqual(counter,1)
        print(counter)
        
        sudoku3: Sudoku = Sudoku(grid)
        counter = validateSudoku(sudoku3,0)
        self.assertGreaterEqual(counter,10)
        print(counter)
