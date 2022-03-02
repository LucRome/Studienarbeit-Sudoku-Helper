from typing import Type, Optional
from sudoku.base import Sudoku, Field

def field_to_value(field: Field) -> Optional[int]:
    return field.get_value()


def checkSudoku(grid):
    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                return False

    # We have a complete grid!
    return True

#A backtracking/recursive function to check all possible combinations of numbers until a solution is found
def validateSudoku(grid: Sudoku, counter):
  if counter >= 10:
    return counter
  #Find next empty cell
  for i in range(0,81):
    row=i//9
    col=i%9
    if (grid.get_field(row,col)).get_value == 0:
      for value in range (1, 10):
        #Check that this value has not already be used on this row
        if not (value in list(map(field_to_value,grid.get_row(row)))):
          #Check that this value has not already be used on this column
          if not (value in list(map(field_to_value, grid.get_column(col)))):
            #Check that this value has not already be used on this 3x3 square
            if not value in list(map(field_to_value,grid.get_block(Sudoku.get_block_nr(row=4, column=7)))):
              grid.get_field(row,col).set_value(value)
              if checkSudoku(grid):
                grid.get_field(row,col).set_value(0)
                return counter + 1
              else:
                   counter = validateSudoku(grid, counter)
                   grid.get_field(row,col).set_value(0)

      return counter
