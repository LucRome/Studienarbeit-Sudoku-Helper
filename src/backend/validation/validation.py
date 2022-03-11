from typing import Type, Optional
from sudoku.base import Sudoku, Field
import time
#Class 
#list map in attribute
#validateSudoku pos mitgeben
#checkSudoku durch i == 81 ersetzten
#name ändern
#select candidate

def field_to_value(field: Field) -> Optional[int]:
    return field.get_value()

class Validation:
  grid = []
  gridBlock = []

  def __init__(self,sudoku):
    for i in range(0,9):
      self.gridBlock.append(list(map(field_to_value, sudoku.get_block(i))))
      self.grid.append(list(map(field_to_value,sudoku.get_row(i))))  

  
  def printSudoku(self):
    print("-----------------------")
    for row in range(0, 9):
        for col in range(0, 9):
            print("[", self.grid[row][col], end ="]")
        print("")
    print("-----------------------")

  def check_sudoku(self):
    for i in range(0,9):
      if None in self.grid[i]:
        return False
    return True  

  def checkBlock(self,row,col,value): 
    Square = []
    for i in range(((row//3)*3),(((row//3)*3)+3)):
      Square.append(self.grid[i][((col//3)*3):(((col//3)*3)+3)]) 
    for i in range (0,3):  
      if (value in Square[i]):
          return False
    return True
      
    


  #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
  def validate_sudoku(self, sudoku:Sudoku, counter, pos):
    if counter >= 2:
      return counter
    #Find next empty cell
    for i in range(pos,81):
      row=i//9
      col=i%9
      fieldvalue = self.grid[row][col]

      if (fieldvalue == None):
        for value in (sudoku.get_field(row,col).get_candidates()):
          #Check that this value has not already be used on this row
          if not (value in self.grid[row]):
            #Check that this value has not already be used on this column
            if not (value in (self.grid[0][col], self.grid[1][col], self.grid[2][col], self.grid[3][col], self.grid[4][col], self.grid[5][col], self.grid[6][col],
                    self.grid[7][col], self.grid[8][col])):
              #Check that this value has not already be used on this 3x3 square
              if self.checkBlock(row=row,col=col,value=value):
                self.grid[row][col] = value 
                if self.check_sudoku():    
                  self.printSudoku()
                  self.grid[row][col] = None
                  return counter + 1
                else:
                  counter = self.validate_sudoku(sudoku, counter, i)
                  self.grid[row][col] = None

        return counter

