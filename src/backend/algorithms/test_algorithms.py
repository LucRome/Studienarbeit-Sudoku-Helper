import unittest
from .algorithms import *
from sudoku.base import Field, Sudoku


class TestAlgorithms(unittest.TestCase):



    def test_unique(self):

        sudokus: List[Sudoku] = []

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
        
        sudoku1: Sudoku = Sudoku(grid)
        
        grid2 = []
        grid2.append([None, 5, None, None, 6, 3, None, 9, None])
        grid2.append([1, None, None, None, 2, 5, None, None, None])
        grid2.append([None, None, 2, None, 1, 8, None, 4, None])
        grid2.append([None, None, None, None, 7, None, None, 2, None])
        grid2.append([None, None, 9, 2, None, None, 6, None, None])
        grid2.append([4, 2, None, 6, 5, None, 3, None, None])
        grid2.append([2, None, 5, None, None, 6, 4, None, None])
        grid2.append([9, None, 1, None, None, 7, None, None, None])
        grid2.append([7, None, 8, None, None, 2, None, None, None])

        sudoku2: Sudoku = Sudoku(grid2)
        
        grid3 = []
        grid3.append([None, None, None, 1, 3, 7, None, None, None])
        grid3.append([7, None, None, 5, 9, 6, 1, 3, None])
        grid3.append([None, None, 9, None, 8, None, None, 6, None])
        grid3.append([None, None, 3, None, 2, None, None, None, None])
        grid3.append([5, None, None, 8, None, None, 9, 2, None])
        grid3.append([None, 2, None, None, 1, None, None, None, None])
        grid3.append([None, None, None, None, None, None, None, None, 8])
        grid3.append([8, 7, 4, None, None, None, None, None, None])
        grid3.append([None, 6, 5, 3, 4, 8, None, None, None])

        sudoku3: Sudoku = Sudoku(grid3)
        
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
        
        sudoku4: Sudoku = Sudoku(grid4)
                
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
       
        sudoku5: Sudoku = Sudoku(grid5)
                
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
       
        sudoku6: Sudoku = Sudoku(grid6)
        
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
        
        grid7 = []
        grid7.append([None, None, None, 7, 1, None, 2, 5, None])
        grid7.append([None, 3, 1, 6, None, None, None, None, 8])
        grid7.append([None, 5, 7, 9, None, None, None, 1, None])
        grid7.append([None, None, None, None, 4, None, None, None, None])
        grid7.append([None, 7, None, None, 6, 2, 1, None, 5])
        grid7.append([None, None, 6, None, 9, 7, 8, None, 2])
        grid7.append([None, None, 9, 2, None, 1, None, 6, None])
        grid7.append([None, None, None, None, 7, 9, 3, 2, 1])
        grid7.append([None, None, None, None, None, 6, None, 8, 9])
        
        sudoku7: Sudoku = Sudoku(grid7)
        
        grid8 = []
        grid8.append([1, 2, None, None, 5, 6, None, 8, None])
        grid8.append([None, None, 5, 9, None, 1, None, None, 6])
        grid8.append([None, None, 6, None, None, 2, 1, None, 5])
        grid8.append([None, 1, 2, None, None, None, 4, None, 7])
        grid8.append([None, 3, None, 1, None, None, None, None, None])
        grid8.append([7, 6, 9, None, 2, None, None, 1, 3])
        grid8.append([None, None, 7, None, 1, 8, None, 9, None])
        grid8.append([None, None, None, 2, None, None, None, None, None])
        grid8.append([None, None, None, None, 4, 3, None, 7, None])
        
        sudoku8: Sudoku = Sudoku(grid8)
               
        grid9 = []
        grid9.append([None, None, None, 9, 2, 3, 1, None, None])
        grid9.append([5, None, 7, None, None, None, None, 8, None])
        grid9.append([2, None, 1, None, 8, None, None, None, None])
        grid9.append([None, 4, None, None, None, None, 6, None, None])
        grid9.append([None, None, None, None, 5, None, None, 2, None])
        grid9.append([None, 1, None, None, None, None, None, None, None])
        grid9.append([8, None, None, None, 7, None, None, None, None])
        grid9.append([None, None, None, 6, None, None, 4, None, None])
        grid9.append([None, None, None, 3, None, None, None, None, 9])
        
        sudoku9: Sudoku = Sudoku(grid9)
        
        grid10 = []
        grid10.append([1, None, None, None, None, None, None, 8, None])
        grid10.append([8, None, 1, None, None, None, None, 2, 4])
        grid10.append([7, None, None, None, None, 3, 1, 5, None])
        grid10.append([None, None, None, None, 4, 1, 6, 9, 2])
        grid10.append([None, 9, None, 6, 7, None, 4, 1, 3])
        grid10.append([4, 1, 6, 2, 3, 9, 8, 7, 5])
        grid10.append([9, None, 1, None, 6, 2, 5, None, 8])
        grid10.append([None, None, None, 3, None, None, 9, None, 1])
        grid10.append([None, 5, None, 9, 1, None, 2, None, 7])
            
        sudoku10: Sudoku = Sudoku(grid10)
        
        grid11 = []
        grid11.append([9, None, None, None, None, None, None, None, 5])
        grid11.append([7, None, 2, None, 1, None, 8, None, None])
        grid11.append([5, None, 4, 8, None, 6, None, None, 2])
        grid11.append([4, None, 7, None, 5, None, 2, None, None])
        grid11.append([8, None, None, 4, None, 3, None, None, 1])
        grid11.append([1, None, 3, None, 8, None, 5, None, None])
        grid11.append([3, 7, None, 9, 4, 2, 1, None, 6])
        grid11.append([6, None, 1, None, 7, None, 4, 2, None])
        grid11.append([2, 4, None, None, None, None, None, None, 7])
        
        sudoku11: Sudoku = Sudoku(grid11)
        
        grid12 = []
        grid12.append([None, 6, None, None, None, 8, 1, 4, None])
        grid12.append([None, 5, None, None, None, 6, 9, 8, None])
        grid12.append([4, 8, None, None, 3, None, 6, None, 5])
        grid12.append([None, 2, 6, None, 8, None, 3, None, 4])
        grid12.append([None, 1, 4, 6, None, 3, 7, None, 8])
        grid12.append([3, 7, 8, None, None, 9, 5, 6, None])
        grid12.append([6, 4, 5, 3, None, 2, 8, None, None])
        grid12.append([1, 9, 2, 8, 7, 5, 4, 3, 6])
        grid12.append([8, 3, 7, None, 6, 4, 2, 5, None])
        
        sudoku12: Sudoku = Sudoku(grid12)
        
        grid13 = []
        grid13.append([None, None, 8, 6, None, None, 2, 1, 9])
        grid13.append([2, None, 6, 9, None, None, 5, 3, 8])
        grid13.append([9, 5, 1, 2, 3, 8, 4, 6, 7])
        grid13.append([4, 8, 2, None, 9, None, 3, 7, 6])
        grid13.append([None, 9, None, 4, 6, 2, 1, 8, 5])
        grid13.append([1, 6, 5, 3, 8, 7, 9, 2, 4])
        grid13.append([8, None, None, None, 2, 9, 6, 4, 3])
        grid13.append([5, None, None, 8, 4, 6, 7, 9, 2])
        grid13.append([6, 2, 9, 7, None, 3, 8, None, 1])
        
        sudoku13: Sudoku = Sudoku(grid13)
        
        grid14 = []
        grid14.append([None, None, None, None, 2, None, None, None, None])
        grid14.append([3, 8, 6, None, None, None, None, 5, 2])
        grid14.append([5, None, None, None, None, 3, None, None, None])
        grid14.append([None, 1, None, None, None, 8, None, 9, None])
        grid14.append([4, None, 8, 9, None, None, 6, None, 7])
        grid14.append([2, None, 9, None, None, 4, None, None, None])
        grid14.append([8, None, None, 7, None, None, 3, 6, None])
        grid14.append([9, None, None, 3, None, 1, None, 4, None])
        grid14.append([None, None, None, None, 5, None, None, None, None])
        
        sudoku14: Sudoku = Sudoku(grid14)
        
        grid15 = []
        grid15.append([None, None, 5, 9, None, 4, None, None, None])
        grid15.append([3, 9, 4, 6, 7, None, None, 5, None])
        grid15.append([7, None, 1, 5, 3, None, 9, 4, 6])
        grid15.append([None, 5, 7, 1, None, None, 4, None, 3])
        grid15.append([2, 3, 9, 8, 4, 5, 6, 7, 1])
        grid15.append([4, 1, None, 7, None, 3, None, 9, None])
        grid15.append([5, 7, None, 4, None, None, 8, None, 9])
        grid15.append([9, None, None, 3, 5, None, None, 1, 4])
        grid15.append([1, 4, None, 2, None, None, None, 6, None])
        
        sudoku15: Sudoku = Sudoku(grid15)
        
        grid16 = []
        grid16.append([6, 4, None, 8, 5, 3, None, 9, None])
        grid16.append([9, None, None, 6, 4, 1, 8, 5, None])
        grid16.append([1, 5, 8, 7, 2, 9, 6, 4, 3])
        grid16.append([3, 2, 5, 1, 6, 7, 9, 8, 4])
        grid16.append([4, None, 1, 9, 8, 2, 3, None, 5])
        grid16.append([8, 9, None, 4, 3, 5, None, 2, None])
        grid16.append([2, None, 9, 5, 1, 8, 4, None, None])
        grid16.append([7, 1, None, 2, 9, 4, 5, None, 8])
        grid16.append([5, 8, 4, 3, 7, 6, 2, 1, 9])
        
        sudoku16: Sudoku = Sudoku(grid16)
        
        grid17 = []
        grid17.append([None, 7, 1, 2, 5, 8, None, None, None])
        grid17.append([None, None, None, 4, 7, 1, 2, None, None])
        grid17.append([2, 4, 5, 3, 6, 9, 7, None, None])
        grid17.append([None, 5, None, 9, 1, 3, 8, 2, None])
        grid17.append([None, None, None, 5, 2, 6, None, 7, None])
        grid17.append([None, 2, None, 8, 4, 7, None, None, 9])
        grid17.append([9, None, None, None, 8, None, None, 6, 2])
        grid17.append([None, 8, 2, None, 3, None, None, None, 7])
        grid17.append([None, None, 4, None, 9, 2, None, None, None])
        
        sudoku17: Sudoku = Sudoku(grid17)
        
        grid18 = []
        grid18.append([None, None, None, 8, 3, 5, 2, 7, None])
        grid18.append([None, None, 7, 9, 4, None, None, 8, None])
        grid18.append([None, 8, None, 1, 7, None, 4, 9, None])
        grid18.append([7, None, 8, 3, 2, 4, 1, 5, None])
        grid18.append([None, None, None, 7, None, None, None, 3, None])
        grid18.append([3, None, None, 5, None, None, 7, 2, None])
        grid18.append([8, 2, 4, 6, 5, 3, 9, 1, 7])
        grid18.append([1, 7, None, 4, 9, 8, None, 6, 2])
        grid18.append([9, None, 6, 2, 1, 7, None, 4, None])
        
        sudoku18: Sudoku = Sudoku(grid18)
        
        grid19 = []
        grid19.append([9, None, 3, 1, None, 2, None, None, 7])
        grid19.append([None, None, None, 7, None, 6, 2, 3, 9])
        grid19.append([2, None, 7, None, 3, None, None, None, 1])
        grid19.append([3, None, None, None, None, 7, 1, 5, 4])
        grid19.append([None, None, 4, None, 2, None, 9, None, 3])
        grid19.append([None, None, None, None, 1, None, 6, None, 2])
        grid19.append([None, 7, None, 2, None, None, 3, None, 5])
        grid19.append([None, 3, None, 8, None, None, 7, None, 6])
        grid19.append([None, None, 1, None, 7, None, 4, None, 8])
        
        sudoku19: Sudoku = Sudoku(grid19)
        
        grid20 = []
        grid20.append([None, None, None, None, 2, 9, None, 4, 1])
        grid20.append([None, 6, None, 1, 5, 8, 7, 2, None])
        grid20.append([2, None, 1, None, 4, 3, None, 5, None])
        grid20.append([None, None, None, 8, 6, None, None, 7, None])
        grid20.append([6,None, None, 9, 3, 4, None, 1, None])
        grid20.append([3, None, None, 2, 7, None, 9, 6, None])
        grid20.append([1, 2, 6, 3, 8, 7, None, 9, None])
        grid20.append([None, None, 9, 5, 1, 6, 2, 3, 7])
        grid20.append([7, 3, 5, 4, 9, 2, 1, 8, 6])
        
        sudoku20: Sudoku = Sudoku(grid20)
        
        grid20_1 = []
        grid20_1.append([5, 9, 8, 4, None, 7, 1, None, None])
        grid20_1.append([None, None, 2, 6, 1, 9, 5, None, 8])
        grid20_1.append([6, None, 1, 5, None, 8, None, None, None])
        grid20_1.append([1, None, 7, 3, 8, 2, None, None, None])
        grid20_1.append([None, None, 6, 1, 9, 4, None, 8, None])
        grid20_1.append([None, 8, 9, 7, 5, 6, 3, 1, None])
        grid20_1.append([8, 6, 5, 2, 7, 3, 4, 9, 1])
        grid20_1.append([9, None, 3, 8, 4, 1, None, None, None])
        grid20_1.append([None, 1, 4, 9, 6, 5, 8, 3, None])

        sudoku20_1: Sudoku = Sudoku(grid20_1)
        
        grid21 = []
        grid21.append([None, None, None, 9, 8, None, 6, None, None])
        grid21.append([4, 6, None, 3, 2, None, 1, 8, 9])
        grid21.append([None, 9, None, None, 1, 6, None, None, 2])
        grid21.append([None, None, 3, 7, 5, 9, None, None, None])
        grid21.append([None, 5, None, 2, 4, 1, 9, None, 3])
        grid21.append([None, None, None, 6, 3, 8, None, 1, None])
        grid21.append([7, None, None, None, None, None, None, None, 1])
        grid21.append([None, None, 1, None, None, None, None, None, None])
        grid21.append([None, None, None, 1, 7, 5, None, 2, 4])

        sudoku21: Sudoku = Sudoku(grid21)

        grid22 = []
        grid22.append([7, None, 6, 9, 1, 8, 4, 3, None])
        grid22.append([None, 1, None, None, None, 6, 9, None, 8])
        grid22.append([None, 8, 9, None, None, 5, None, None, None])
        grid22.append([8, None, None, None, 6, None, None, None, None])
        grid22.append([6, None, None, None, 4, None, 5, None, None])
        grid22.append([1, 7, None, None, 9, 3, None, 2, None])
        grid22.append([5, 3, 7, 1, 8, 4, 2, 6, 9])
        grid22.append([9, 6, 8, 3, 5, 2, 7, None, None])
        grid22.append([2, 4, 1, 6, 7, 9, None, None, None])

        sudoku22: Sudoku = Sudoku(grid22)
        
        grid23 = []
        grid23.append([None, 6, 9, None, None, 1, None, 3, None])
        grid23.append([None, 3, 4, None, 5, None, None, 1, None])
        grid23.append([None, 1, None, None, 3, 7, None, None, 4])
        grid23.append([None, None, None, 3, 7, None, None, 9, None])
        grid23.append([None, 7, 6, 1, 8, None, None, None, 5])
        grid23.append([1, None, None, 2, 6, None, 7, None, None])
        grid23.append([None, None, 1, 7, None, None, None, 6, None])
        grid23.append([6, None, 7, None, None, None, None, 5, None])
        grid23.append([4, None, None, 5, 1, 6, None, 7, None])

        sudoku23: Sudoku = Sudoku(grid23)
        
        grid24 = []
        grid24.append([None, None, 8, None, 5, None, 4, 3, None])
        grid24.append([None, None, 3, 8, 7, None, 2, None, 5])
        grid24.append([None, None, None, 9, None, None, 1, 8, 7])
        grid24.append([None, 2, None, None, None, 7, 9, 1, None])
        grid24.append([None, None, None, 5, None, None, 6, 2, None])
        grid24.append([9, None, 6, None, None, None, None, None, None])
        grid24.append([4, None, None, None, None, None, 3, None, 2])
        grid24.append([None, None, None, 1, 2, 6, 8, 4, None])
        grid24.append([None, 8, 2, 3, 4, None, None, None, None])

        sudoku24: Sudoku = Sudoku(grid24)
        
        grid25 = []
        grid25.append([None, None, 4, 3, None, 2, None, 1, 8])
        grid25.append([8, None, None, None, None, None, None, 7, None])
        grid25.append([None, None, 3, 8, 9, None, 4, 5, None])
        grid25.append([6, 2, 8, None, None, None, 5, None, 4])
        grid25.append([5, 3, 9, 4, 6, 8, 1, 2, 7])
        grid25.append([4, None, None, 5, 2, None, 8, 6, None])
        grid25.append([None, None, None, None, 1, None, None, None, None])
        grid25.append([None, None, 5, None, None, None, 7, None, 1])
        grid25.append([1, None, None, 7, 8, None, None, None, None])

        sudoku25: Sudoku = Sudoku(grid25)
        
        grid26 = []
        grid26.append([1, 2, None, 5, 7, 9, None, None, None])
        grid26.append([None, 3, 9, 2, 4, None, 5, None, 7])
        grid26.append([5, None, 7, 6, 3, 8, 9, 2, None])
        grid26.append([None, None, 6, 7, None, None, None, None, None])
        grid26.append([None, 7, 3, None, None, None, 2, None, None])
        grid26.append([None, 5, None, 3, None, 4, 7, None, 9])
        grid26.append([7, None, None, None, None, None, 8, 9, 3])
        grid26.append([None, 9, None, None, None, 3, 1, 7, 5])
        grid26.append([3, None, 5, 9, None, 7, 6, 4, 2])

        sudoku26: Sudoku = Sudoku(grid26)
        
           
        grid252 = []
        grid252.append([None, 8, None, 6, 5, 4, None, None, 1])
        grid252.append([None, None, None, 2, 3, None, None, None, None])
        grid252.append([4, None, 3, 8, 9, None, None, 5, None])
        grid252.append([3, None, 8, None, 4, 5, None, None, 7])
        grid252.append([None, None, 9, None, 6, 2, 1, None, 8])
        grid252.append([2, None, None, None, 8, None, None, None, None])
        grid252.append([None, None, 4, 5, 1, 8, None, 7, None])
        grid252.append([1, 7, 5, None, 2, 6, None, None, None])
        grid252.append([8, None, None, 4, 7, None, None, 1, None])

        sudoku252: Sudoku = Sudoku(grid252)     
        
        sudokus = [
            sudoku1,
            sudoku2,
            sudoku3,
            sudoku4,
            sudoku5,
            sudoku6,
            sudoku7,
            sudoku8,
            sudoku9,
            sudoku10,
            sudoku11,
            sudoku12,
            sudoku13,
            sudoku14,
            sudoku15,
            sudoku16,
            sudoku17,
            sudoku18,
            sudoku19,
            sudoku20,
            sudoku21,
            sudoku22,
            sudoku23,
            sudoku24,
            sudoku25,
            sudoku26,
            sudoku252
        ]
        
        algos:List[Algorithm] = []
        
        for s in sudokus:
            s.select_candidates()
            if s == sudoku17:
                s.get_field(6,6).remove_candidate(1)
                s.get_field(6,6).remove_candidate(3)
            if s == sudoku26:
                s.get_field(5,4).remove_candidate(1)
                s.get_field(5,4).remove_candidate(2)
            algos.append(Algorithm(s))
            print('.....')
            
        self.assertTrue(algos[0].algorithm_1()[0])
        self.assertTrue(algos[1].algorithm_2()[0])
        #self.assertTrue(algos[2].algorithm_3()[0])
        self.assertTrue(algos[3].algorithm_4()[0])
        self.assertTrue(algos[4].algorithm_5()[0])
        self.assertTrue(algos[5].algorithm_6()[0])
        self.assertTrue(algos[6].algorithm_7()[0])
        self.assertTrue(algos[7].algorithm_8()[0])
        self.assertTrue(algos[8].algorithm_9()[0])
        self.assertTrue(algos[9].algorithm_10()[0])
        self.assertTrue(algos[10].algorithm_11_1()[0])
        self.assertTrue(algos[11].algorithm_12()[0])
        self.assertTrue(algos[12].algorithm_13()[0])
        self.assertTrue(algos[13].algorithm_14()[0])
        self.assertTrue(algos[14].algorithm_15_1()[0])
        self.assertTrue(algos[15].algorithm_16()[0])
        self.assertTrue(algos[16].algorithm_17()[0])
        self.assertTrue(algos[17].algorithm_18()[0])
        self.assertTrue(algos[19].algorithm_20()[0])
        self.assertTrue(algos[20].algorithm_21()[0])
        self.assertTrue(algos[21].algorithm_22()[0])
        self.assertTrue(algos[22].algorithm_23()[0])
        self.assertTrue(algos[23].algorithm_24()[0])
        self.assertTrue(algos[24].algorithm_25_1()[0])
        self.assertTrue(algos[25].algorithm_26()[0])
        #self.assertTrue(algos[26].algorithm_25_2()[0])
        
        algo = Algorithm(sudoku24)
        bol,string = algo.algorithm_24()
        print(bol,string)
        
        # noch zu testen (11_2 15_2 25_2)
        