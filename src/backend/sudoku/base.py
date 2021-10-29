"""
Base Classes for Sudoku
"""

from typing import List, Optional
from exceptions import *
from math import floor

class Field:
    """
    represents a single field 
    with a value and the candidates
    """
    __value: Optional[int]
    __candidates: List[int] = list()

    def set_value(self, val: int) -> None:
        if val < 0 or val > 9:
            raise WrongFieldValueExcetion(val)
        else:
            self.__value = val
    
    def add_candidate(self, val: int) -> None:
        if val < 0 or val > 9:
            raise WrongFieldCandidateException(val)
        else:
            if val not in self.__candidates:
                self.__candidates.append(val)
    
    def remove_candidate(self, val: int) -> None:
        try:
            self.__candidates.remove(val)
        except ValueError:
            pass

    def get_value(self) -> Optional[int]:
        return self.__value
    
    def get_candidates(self) -> List[int]:
        return self.__candidates
    

class Sudoku:
    """
    Class for the complete Sudoku Field
    Orientation: See GitHub Wiki
    """
    fields: List[List[Field]] = list(list())
    
    def __init__(self) -> None:
        for column in range(0, 8):
            for row in range(0,8):
                self.fields[column][row] = Field()

    def get_field(self, row: int, column: int) -> Field:
        if row < 0 or row > 8 or column < 0 or column > 8:
            raise OutOfFieldsException()
        return self.fields[column][row]

    def get_row(self, row: int) -> List[Field]:
        if row < 0 or row > 8:
            raise OutOfFieldsException()
        return self.fields[row]

    def get_column(self, column: int) -> List[Field]:
        if column < 0 or column > 8:
            raise OutOfFieldsException()
        ret: List[Field] = list()
        for row in range(0, 8):
            ret.append(self.fields[column][row])
        return ret
    
    def get_block(self, block_nr: int) -> List[Field]:
        if block_nr < 0 or block_nr > 8:
            raise OutOfFieldsException()

        # Determine the rows and columns
        columns: range
        if (block_nr % 3) == 0:
            columns = range(0,2)
        elif (block_nr % 3) == 1:
            columns = range(3, 5)
        else:
            columns = range(6, 8)
        rows: range
        if block_nr <= 2:
            rows = range(0,2)
        elif block_nr <= 5:
            rows = range(3, 5)
        else:
            rows = range(6, 8)
        
        # fill the return list
        ret: List[Field] = list()
        for x in columns:
            for y in rows:
                List.append(self.fields[columns][rows])

    def get_block_nr(row: int, column: int) -> int:
        if row < 0 or row > 8 or column < 0 or column > 8:
            raise OutOfFieldsException()
        x: int = floor(column/3)
        y: int = floor(row/3)
        return y*3 + x