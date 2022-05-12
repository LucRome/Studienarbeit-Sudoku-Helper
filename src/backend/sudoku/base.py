"""
Base Classes for Sudoku
"""

from typing import List, Optional, Tuple
from .exceptions import *
from math import floor

FIELD_VALUE_MIN = 1
FIELD_VALUE_MAX = 9
ALL_FIELD_VALUES = range(FIELD_VALUE_MIN, FIELD_VALUE_MAX + 1)

def list_intersection(a: List[int], b: List[int]) -> List[int]:
    """
    Creates the Intersection of the two Lists
    """
    res = list()
    for val in a:
        if val in b:
            res.append(val)
    return res
    
class Field:
    """
    represents a single field 
    with a value and the candidates
    """
    __value: Optional[int]
    __candidates: List[int]
    __coordinates: Tuple[int, int]

    def __init__(self, coordinates: Tuple[int, int],value: Optional[int] = None):
        self.__candidates, self.__coordinates = list(), coordinates
        if value is not None:
            self.set_value(value)
        else:
            self.remove_value()
    
    def get_coordinates(self) -> Tuple[int, int]:
        return self.__coordinates

    def set_value(self, val: int) -> None:
        if val is not None and (val < FIELD_VALUE_MIN or val > FIELD_VALUE_MAX):
            raise WrongFieldValueException(val)
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
    
    def set_candidates(self, vals: List[int]) -> None:
        self.__candidates.clear()
        for val in vals:
            self.add_candidate(val)

    def get_value(self) -> Optional[int]:
        return self.__value
    
    def get_candidates(self) -> List[int]:
        return self.__candidates
    

def set_all_candidates(fields: List[Field], candidates: List[int]) -> None:
    """
    Sets the candidates as candidates of all fields without a value
    """
    for field in fields:
        if field.get_value() is None:
            field.set_candidates(candidates)

def intersect_all_candidates(fields: List[Field], candidates: List[int]) -> None:
    """
    Sets the intersection of candidates and the fields candidates as 
    candidates of the field
    (For all fields)
    """
    for field in fields:
        if field.get_value() is None:
            field.set_candidates(list_intersection(candidates, field.get_candidates()))

def value_in_section(fields: List[Field], val: int) -> bool:
    """
    checks whether the given Field value is present in the given list of Fields
    """
    for field in fields:
        if field.get_value() == val:
            return  True
    return False

NINE_RANGE = range(0,9)
class Sudoku:
    """
    Class for the complete Sudoku Field
    Orientation: See GitHub Wiki
    """
    fields: List[List[Field]]
    
    def __init__(self, values: Optional[List[List[Optional[int]]]] = None) -> None:
        self.fields = list()
        if values is None:
            for row in NINE_RANGE:
                self.fields.append(list())
                for column in NINE_RANGE:
                    self.fields[row].append(Field(coordinates=(row, column)))
        else:
            for row in NINE_RANGE:
                self.fields.append(list())
                for column in NINE_RANGE:
                    self.fields[row].append(Field(coordinates=(row, column),value=values[row][column]))
        

    def get_field(self, row: int, column: int) -> Field:
        if row not in NINE_RANGE or column not in NINE_RANGE:
            raise OutOfFieldsException()
        return self.fields[row][column]

    def get_row(self, row: int) -> List[Field]:
        if row not in NINE_RANGE:
            raise OutOfFieldsException()
        return self.fields[row]

    def get_column(self, column: int) -> List[Field]:
        if column not in NINE_RANGE:
            raise OutOfFieldsException()
        ret: List[Field] = list()
        for row in range(0, 9):
            ret.append(self.get_field(row, column))
        return ret
    
    def get_block(self, block_nr: int) -> List[Field]:
        if block_nr not in NINE_RANGE:
            raise OutOfFieldsException()

        rows, columns = Sudoku.get_block_ranges(block_nr)
        
        # fill the return list
        ret: List[Field] = list()
        for y in rows:
            for x in columns:
                ret.append(self.get_field(row=y, column= x))
        return ret

    def get_block_nr(row: int, column: int) -> int:
        if row not in NINE_RANGE or column not in NINE_RANGE:
            raise OutOfFieldsException()
        x: int = floor(column/3)
        y: int = floor(row/3)
        return y*3 + x
    
    def get_block_ranges(block_nr: int) -> Tuple[range, range]:
        """
        Get the ranges for row and column for the blocks
        """
        row_start = (block_nr // 3) * 3
        col_start = (block_nr % 3) * 3

        return (range(row_start, row_start+3), range(col_start, col_start+3))
    
    def select_candidates(self) -> None:
        """
        Adds all the candidates to the fields
        """

        # List of all candidates (reused)
        candidates: List[int] = list()

        # First select all the candidates by row
        for y in NINE_RANGE:
            candidates.clear()
            row = self.get_row(y)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(row, val):
                    candidates.append(val)
            set_all_candidates(row, candidates)
        
        # intersect with candidates by column
        for x in NINE_RANGE:
            candidates.clear()
            col = self.get_column(x)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(col, val):
                    candidates.append(val)
            intersect_all_candidates(col, candidates)

        # intersect with candidates by block
        for i in NINE_RANGE:
            candidates.clear()
            blk = self.get_block(i)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(blk, val):
                    candidates.append(val)
            intersect_all_candidates(blk, candidates)

    def recalculate_candidates(self) -> None:
        """
        Only removes wrong candidates from fields, adds no new ones
        """
        # List of all candidates (reused)
        candidates: List[int] = list()

        # by row
        for y in NINE_RANGE:
            candidates.clear()
            row = self.get_row(y)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(row, val):
                    candidates.append(val)
            intersect_all_candidates(row, candidates)
        
        # intersect with candidates by column
        for x in NINE_RANGE:
            candidates.clear()
            col = self.get_column(x)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(col, val):
                    candidates.append(val)
            intersect_all_candidates(col, candidates)

        # intersect with candidates by block
        for i in NINE_RANGE:
            candidates.clear()
            blk = self.get_block(i)
            for val in ALL_FIELD_VALUES:
                if not value_in_section(blk, val):
                    candidates.append(val)
            intersect_all_candidates(blk, candidates)