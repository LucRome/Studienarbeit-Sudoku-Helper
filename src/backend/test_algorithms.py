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
        
        
        grid12 = []
        grid12.append([None, None, 8, 6, None, None, 2, 1, 9])
        grid12.append([2, None, 6, 9, None, None, 5, 3, 8])
        grid12.append([9, 5, 1, 2, 3, 8, 4, 6, 7])
        grid12.append([4, 8, 2, None, 9, None, 3, 7, 6])
        grid12.append([None, 9, None, 4, 6, 2, 1, 8, 5])
        grid12.append([1, 6, 5, 3, 8, 7, 9, 2, 4])
        grid12.append([8, None, None, None, 2, 9, 6, 4, 3])
        grid12.append([5, None, None, 8, 4, 6, 7, 9, 2])
        grid12.append([6, 2, 9, 7, None, 3, 8, None, 1])
        
        grid13 = []
        grid13.append([None, 6, None, None, None, 8, 1, 4, None])
        grid13.append([None, 5, None, None, None, 6, 9, 8, None])
        grid13.append([4, 8, None, None, 3, None, 6, None, 5])
        grid13.append([None, 2, 6, None, 8, None, 3, None, 4])
        grid13.append([None, 1, 4, 6, None, 3, 7, None, 8])
        grid13.append([3, 7, 8, None, None, 9, 5, 6, None])
        grid13.append([6, 4, 5, 3, None, 2, 8, None, None])
        grid13.append([1, 9, 2, 8, 7, 5, 4, 3, 6])
        grid13.append([8, 3, 7, None, 6, 4, 2, 5, None])
        
        
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

        sudoku1: Sudoku = Sudoku(grid13)
        sudoku1.select_candidates()
        #sudoku1.get_field(6,6).remove_candidate(1) #17
        #sudoku1.get_field(6,6).remove_candidate(3) #17
        algo = Algorithm(sudoku1)
        bol,stri = algo.algorithm_12()
        print('Bool:',bol)
        print('String:',stri)