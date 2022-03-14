from typing import Tuple, Optional
from sudoku.base import Sudoku, Field

def field_to_value(field: Field) -> Optional[int]:
    return field.get_value()

class Validation:
  grid = []

  def __init__(self,sudoku):
    for i in range(0,9):
      self.grid.append(list(map(field_to_value,sudoku.get_row(i))))  

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
      
  def validate(self, sudoku:Sudoku) -> Tuple[bool, Optional[str]]:
    counter = self.validate_sudoku(sudoku,0,0)
    if counter == 0:
      return (False, f'The Sudoku is not valid! No Solutions exist!')
    elif counter == 1:
      return (True, None)
    else:
      return (False, f'The Sudoku is not valid! Multiple Solutions exist!')  

        


  def validate_sudoku(self, sudoku:Sudoku, counter, pos):
    if counter >= 2:
      return counter
    for i in range(pos,81):
      row=i//9
      col=i%9
      fieldvalue = self.grid[row][col]
      #Find next empty cell
      if (fieldvalue == None):
        #Check if Value is a possible Candidate
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
                  self.grid[row][col] = None
                  return counter + 1
                else:
                  counter = self.validate_sudoku(sudoku, counter, i)
                  self.grid[row][col] = None

        return counter

