"""
Base Classes for Sudoku
"""

from typing import List, Optional
from exceptions import *
from math import floor

FIELD_VALUE_MIN = 1
FIELD_VALUE_MAX = 9
class Field:
    """
    represents a single field 
    with a value and the candidates
    """
    __value: Optional[int]
    __candidates: List[int] = list()

    def __init__(self, value: Optional[int] = None):
        if value is not None:
            self.set_value(value)
        else:
            self.remove_value()

    def set_value(self, val: int) -> None:
        if val < FIELD_VALUE_MIN or val > FIELD_VALUE_MAX:
            raise WrongFieldValueExcetion(val)
        else:
            self.__value = val
    
    def remove_value(self) -> None:
        self.__value = None
    
    def add_candidate(self, val: int) -> None:
        if val < FIELD_VALUE_MIN or val > FIELD_VALUE_MAX:
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
    fields: List[List[Field]]
    
    def __init__(self, values: Optional[List[List[Optional[int]]]] = None) -> None:
        self.fields = list()
        if values is None:
            for column in range(0, 9):
                self.fields.append(list())
                for row in range(0,9):
                    self.fields[column].append(Field())
        else:
            for column in range(0,9):
                self.fields.append(list())
                for row in range(0,9):
                    self.fields[column].append(Field(values[row][column]))

    def get_field(self, row: int, column: int) -> Field:
        if row < 0 or row > 8 or column < 0 or column > 8:
            raise OutOfFieldsException()
        return self.fields[column][row]

    def get_row(self, row: int) -> List[Field]:
        if row < 0 or row > 8:
            raise OutOfFieldsException()
        ret: List[Field] = list()
        for column in range(0, 9):
            ret.append(self.fields[column][row])
        return ret

    def get_column(self, column: int) -> List[Field]:
        if column < 0 or column > 8:
            raise OutOfFieldsException()
        return self.fields[column]
    
    def get_block(self, block_nr: int) -> List[Field]:
        if block_nr < 0 or block_nr > 8:
            raise OutOfFieldsException()

        # Determine the rows and columns
        columns: range
        if (block_nr % 3) == 0:
            columns = range(0,3)
        elif (block_nr % 3) == 1:
            columns = range(3, 6)
        else:
            columns = range(6, 9)
        rows: range
        if block_nr <= 2:
            rows = range(0,3)
        elif block_nr <= 5:
            rows = range(3, 6)
        else:
            rows = range(6, 9)
        
        # fill the return list
        ret: List[Field] = list()
        for y in rows:
            for x in columns:
                ret.append(self.fields[x][y])
        return ret

    def get_block_nr(row: int, column: int) -> int:
        if row < 0 or row > 8 or column < 0 or column > 8:
            raise OutOfFieldsException()
        x: int = floor(column/3)
        y: int = floor(row/3)
        return y*3 + x