from sudoku.base import Sudoku, Field, NINE_RANGE
from typing import List, Tuple, Literal, Dict
from enum import Enum

# TODO: implement Function that removes the given candidates from the fields in the given unit, except the given fields

class UnitType(Enum):
    ROW = 'row'
    COLUMN = 'column'
    BLOCK = 'block'


def get_unit(type: UnitType, nr: int, excluded_fields: List[Tuple[int, int]] = []) -> List[Tuple[int, int]]:
    unit: List[Tuple[int, int]] = list()  # the coordinates of the unit fields (except the excluded ones)

    if type == UnitType.ROW:
        for col in NINE_RANGE:
            if (nr, col) not in excluded_fields:
                unit.append((nr, col))
    elif type == UnitType.COLUMN:
        for row in NINE_RANGE:
            if (row, nr) not in excluded_fields:
                unit.append((nr, col))
    elif type == UnitType.BLOCK:
        rows, cols = Sudoku.get_block_ranges(nr)
        for row in rows:
            for col in cols:
                if (row, col) not in excluded_fields:
                    unit.append((row, col))

    return unit

def remove_candidates_from_fields_in_unit(sudoku: Sudoku,type: UnitType, nr: int,
    candidates_to_remove: List[int], excluded_fields: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    """
    Removes the given candidates from the fields of the given unit (except the excluded fields)
    :param sudoku: the sudoku
    :param type: The unit Type (row/block/column)
    :param nr: The nr of the unit (row nr/block nr/column nr)
    :param candidates_to_remove: The list of the candidates to remove
    :param excluded fields: The coordinates of the fields to exclude
    :returns: Dictionary of all the removed candidates
    """
    
    unit = get_unit(type, nr, excluded_fields)

    removed_candidates: Dict[int, List[int]] = dict() #Key: y*10+x
    for (y,x) in unit:
        field = sudoku.get_field(y, x)
        key = y*10 + x
        field_candidates = field.get_candidates()
        for v in candidates_to_remove:
            if v in field_candidates:
                # Add to dict and remove
                field.remove_candidate(v)
                rm = removed_candidates.get(key)
                if rm:
                    rm.append(v)
                else:
                    removed_candidates.update({key: [v]})

    return removed_candidates

def enforce_hidden_algs(sudoku: Sudoku, type: UnitType, nr: int,
    candidates_to_lock: List[int]) -> Dict[int, List[int]]:
    """
    Enforces the hidden algorithms (e.g. hidden pair) 
    -> sets the candidates in the fields if they are the only ones and removes the others from the fields
    :param sudoku: Sudoku class
    :param type: Type of the unit
    :param nr: Number of the unit
    :param candidates_to_lock: The candidates to set as the field candidates
    :returns: Dictionary of all the removed candidates (key: Field coordinates (key = y*10 + x))
    """

    unit = get_unit(type, nr)
    removed_candidates: Dict[int, List[int]] = dict() #Key: y*10+x

    for (y, x) in unit:
        field_candidates = sudoku.get_field(y, x).get_candidates()
        if all(list(map(lambda c: c in field_candidates, candidates_to_lock))):
            # remove all other candidates
            rm: List[int] = list()
            for c in field_candidates:
                if c not in candidates_to_lock:
                    rm.append(c)
            for c in rm:  # needs to be seperated, otherwise errors occur
                field_candidates.remove(c)

            removed_candidates.update({y*10+x: rm})
    
    return removed_candidates

        