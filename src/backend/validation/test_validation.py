import unittest
from validation.validation import *
from sudoku.base import Field, Sudoku


class TestValidateSudoku(unittest.TestCase):



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

#sudoku with 2 solutions
        grid2 = []
        grid2.append([9, None, 6, None, 7, None, 4, None, 3])
        grid2.append([None, None, None, 4, None, None, 2, None, None])
        grid2.append([None, 7, None, None, 2, 3, None, 1, None])
        grid2.append([5, None, None, None, None, None, 1, None, None])
        grid2.append([None, 4, None, 2, None, 8, None, 6, None])
        grid2.append([None, None, 3, None, None, None, None, None, 5])
        grid2.append([None, 3, None, 7, None, None, None, 5, None])
        grid2.append([None, None, 7, None, None, 5, None, None, None])
        grid2.append([4, None, 5, None, 1, None, 7, None, 8])


#sudoku with > 2NoneNoneNoneNone solutions
        grid3 = []
        grid3.append([None, None, None, None, None, None, None, 1, 2])
        grid3.append([None, None, None, None, 3, 5, None, None, None])
        grid3.append([None, None, None, 6, None, None, None, 7, None])
        grid3.append([7, None, None, None, None, None, 3, None, None])
        grid3.append([None, None, None, 4, None, 8, None, None, None])
        grid3.append([1, None, None, None, None, None, None, None, None])
        grid3.append([None, None, None, 1, 2, None, None, None, None])
        grid3.append([None, 8, None, None, None, None, None, 4, None])
        grid3.append([None, 5, None, None, None, None, 6, None, None])
        
        




        # Correct sudoku
        grid4 = [
                [None, 5, None, None, 3, 2, 4, 9, None],
                [None, 9, 6, None, None, None, 2, 1, None],
                [None, 8, None, 1, None, 6, 7, None, 3],
                [None, None, None, None, 6, None, 3, 7, None],
                [None, 6, None, None, None, 9, 1, None, 5],
                [None, 1, None, 3, 7, None, None, 6, None],
                [None, None, None, None, None, None, 5, 3, None],
                [8, 3, None, 2, 5, 7, None, 4, None],
                [5, None, None, 6, None, 3, 8, None, 7],
        ]
        # Correct sudoku
        grid5 = [
                [None, 5, 2, None, None, None, 6, None, None],
                [None, None, None, 3, None, None, None, 8, None],
                [None, None, None, 1, None, None, None, None, None],
                [6, 4, None, None, None, None, 5, None, None],
                [None, None, None, None, 2, 9, None, None, None],
                [None, None, None, 7, None, None, None, None, None],
                [1, None, 9, None, None, None, None, 3, None],
                [None, None, None, None, 5, None, 4, None, None],
                [None, None, None, None, None, None, None, None, None],
        ]
        sudoku1: Sudoku = Sudoku(grid)
        sudoku1.select_candidates()
        val = Validation(sudoku1)
        bol,msg = val.validate(sudoku1)
        self.assertTrue(bol,2)

        sudoku2: Sudoku = Sudoku(grid2)
        sudoku2.select_candidates()
        val = Validation(sudoku2)
        bol,msg = val.validate(sudoku2)
        self.assertFalse(bol,2)
        sudoku3: Sudoku = Sudoku(grid3)
        sudoku3.select_candidates()
        val = Validation(sudoku3)
        bol,msg = val.validate(sudoku3)
        self.assertFalse(bol,2)
       
        
        sudoku4: Sudoku = Sudoku(grid4)
        val = Validation(sudoku4)
        sudoku4.select_candidates()
        bol,msg = val.validate(sudoku4)
        self.assertTrue(bol)
        
        sudoku5: Sudoku = Sudoku(grid5)
        val = Validation(sudoku5)
        sudoku5.select_candidates()
        bol,msg = val.validate(sudoku5)
        self.assertTrue(bol)

