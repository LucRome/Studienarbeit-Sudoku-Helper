from typing import Type, Optional
from sudoku.base import Sudoku, Field

#Class 
#list map in attribute
#validateSudoku pos mitgeben
#checkSudoku durch i == 81 ersetzten
#name ändern
#select candidate

def field_to_value(field: Field) -> Optional[int]:
    return field.get_value()

class Validation:
      
  gridRow = []
  gridCol = []
  gridBlock = []
  
  def __init__(self, grid: Sudoku):
    for i in range(0,9):
      self.gridRow.append(list(map(field_to_value,grid.get_row(i))))
      self.gridCol.append(list(map(field_to_value, grid.get_column(i))))
      self.gridBlock.append(list(map(field_to_value,grid.get_block(i))))

  def check_sudoku(self):
      for row in range(0, 9):
          for col in range(0, 9):
              if self.gridRow[row][col] == None:
                  return False

      # We have a complete grid!
      return True

  #A backtracking/recursive function to check all possible combinations of numbers until a solution is found
  def validate_sudoku(self, grid: Sudoku, counter, pos):
    if counter >= 2:
      return counter
    #Find next empty cell
    for i in range(pos,81):
      row=i//9
      col=i%9
      fieldvalue = grid.get_field(row,col).get_value()

      if (fieldvalue == None):
        for value in range (1, 10):
          #Check that this value has not already be used on this row
          if not (value in self.gridRow[row]):
            #Check that this value has not already be used on this column
            if not (value in self.gridCol[col]):
              #Check that this value has not already be used on this 3x3 square
              if not (value in self.gridBlock[Sudoku.get_block_nr(row,col)]):
                grid.get_field(row,col).set_value(value)
                self.gridRow[row][col] = value
                self.gridCol[col][row] = value
                self.gridBlock[Sudoku.get_block_nr(row,col)][(row%3)+(col%3)] = value
                if self.check_sudoku():
                  grid.get_field(row,col).set_value(None)
                  self.gridRow[row][col] = None
                  self.gridCol[col][row] = None
                  self.gridBlock[Sudoku.get_block_nr(row,col)][(row%3)+(col%3)] = None
                  return counter + 1
                else:
                  counter = self.validate_sudoku(grid, counter, i+1)
                  grid.get_field(row,col).set_value(None)
                  self.gridRow[row][col] = None
                  self.gridCol[col][row] = None
                  self.gridBlock[Sudoku.get_block_nr(row,col)][(row%3)+(col%3)] = None

        return counter
