from sudoku.base import Sudoku, Field, NINE_RANGE
from typing import List, Tuple, Literal, Dict
from enum import Enum

# TODO: implement Function that removes the given candidates from the fields in the given unit, except the given fields

class UnitType(Enum):
    ROW = 'row'
    COLUMN = 'column'
    BLOCK = 'block'

def remove_candidates_from_fields_in_unit(sudoku: Sudoku,type: UnitType, nr: int,
    candidates_to_remove: List[int], excluded_fields: List[Tuple[int, int]]) -> Dict[Tuple[int, int], List[int]]:
    """
    Removes the given candidates from the fields of the given unit (except the excluded fields)
    :param sudoku: the sudoku
    :param type: The unit Type (row/block/column)
    :param nr: The nr of the unit (row nr/block nr/column nr)
    :param candidates_to_remove: The list of the candidates to remove
    :param excluded fields: The coordinates of the fields to exclude
    :returns: Dictionary of all the removed candidates
    """
    
    unit: List[Tuple[int, int]] = list()  # the fields in the unit with their coordinates (except the excluded ones)

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


        