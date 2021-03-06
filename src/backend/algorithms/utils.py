import math
from sudoku.base import Sudoku, Field, NINE_RANGE
from typing import List, Tuple, Literal, Dict, Optional
from enum import Enum


def has_removed_candidates(removed_candidates: Dict[int, List[int]]) -> bool:
    """
    Checks whether some candidates where actually removed
    """
    return any([len(l) > 0 for l in removed_candidates.values()])

class UnitType(Enum):
    ROW = 'row'
    COLUMN = 'column'
    BLOCK = 'block'


def get_unit(type: UnitType, nr: int, excluded_fields: List[Tuple[int, int]] = []) -> List[Tuple[int, int]]:
    unit: List[Tuple[int, int]] = list()  # the coordinates of the unit fields (except the excluded ones)

    # make sure, that excluded fields are Tuples
    for f in excluded_fields:
        if not isinstance(f, tuple):
            raise TypeError(f'Fields must be tuples, not: {f.__class__}')
    if type == UnitType.ROW:
        for col in NINE_RANGE:
            if (nr, col) not in excluded_fields:
                unit.append((nr, col))
    elif type == UnitType.COLUMN:
        for row in NINE_RANGE:
            if (row, nr) not in excluded_fields:
                unit.append((row, nr))
    elif type == UnitType.BLOCK:
        rows, cols = Sudoku.get_block_ranges(nr)
        for row in rows:
            for col in cols:
                if (row, col) not in excluded_fields:
                    unit.append((row, col))

    return unit


def coordinates_to_key(y: int, x: int) -> int:
    """
    Transforms the Coordinates into a key for the dictionary
    """
    return y*10 + x


def key_to_coordinates(key: int) -> Tuple[int, int]:
    """
    Transforms the key for the dictionary back into coordinates
    :returns: (y, x)
    """
    return (key//10, key%10)

def remove_candidates_from_fields(sudoku: Sudoku, fields: List[Tuple[int, int]], candidates_to_remove: List[int], except_fields: Optional[List[Tuple[int, int]]] = None) -> Dict[int, List[int]]:
    """
    Removes the given candidates from the given fields
    :param sudoku: the sudoku
    :param fields: Coordinates of the fields to remove the candidates from
    :param candidates: candidates to remove
    """
    removed_candidates: Dict[int, List[int]] = dict() #Key: y*10+x
    for (y,x) in fields:
        if except_fields and (y,x) in except_fields:
            continue
        field = sudoku.get_field(y, x)
        key = coordinates_to_key(y, x)
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
        key = coordinates_to_key(y, x)
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

def recalc_candidates_with_new_value(sudoku: Sudoku, field: Tuple[int, int]) -> Dict[int, List[int]]:
    """
    Removes the obsolete candidates from the sudoku, when a new value is set
    :param sudoku: the Sudoku
    :param field: the field with the new value (y, x)
    :returns: a Dictionary of all the deleted candidates, sorted by field (key: y*10+x)
    """
    y,x = field
    value_to_remove = [sudoku.get_field(y, x).get_value()]
    dict_row = remove_candidates_from_fields_in_unit(sudoku, UnitType.ROW, y, value_to_remove, [])
    dict_col = remove_candidates_from_fields_in_unit(sudoku, UnitType.COLUMN, x, value_to_remove, [])
    dict_block = remove_candidates_from_fields_in_unit(sudoku, UnitType.BLOCK, Sudoku.get_block_nr(y, x), value_to_remove, [])

    return {**dict_row, **dict_col, **dict_block}  # merge the dicts (keys that are double are overwritten)


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
        if any(list(map(lambda c: c in field_candidates, candidates_to_lock))):
            # remove all other candidates
            rm: List[int] = list()
            for c in field_candidates:
                if c not in candidates_to_lock:
                    rm.append(c)
            for c in rm:  # needs to be seperated, otherwise errors occur
                field_candidates.remove(c)

            removed_candidates.update({y*10+x: rm})
    
    return removed_candidates



        
def find_chain_12(sudoku:Sudoku,field:Field,value:int) -> Tuple[bool,List[Field]]:  
    chain: List[Field] = list()
    col = sudoku.get_column(field.get_coordinates()[1])
    chain.append(field)
    for i in NINE_RANGE:
        if value in col[i].get_candidates() and col[i].get_coordinates()[0] != field.get_coordinates()[0]:
            chain.append(col[i])
    if len(chain)>=3:
        return False, chain
    if len(chain) < 2:
        return True, None
    block =  sudoku.get_block(Sudoku.get_block_nr(chain[1].get_coordinates()[0],chain[1].get_coordinates()[1]))
    for i in NINE_RANGE:
        if value in block[i].get_candidates() and block[i].get_coordinates()[0]!= chain[1].get_coordinates()[0] and block[i].get_coordinates()[0]!= chain[0].get_coordinates()[0]:
            chain.append(block[i])
    if len(chain) < 3:
            return True, None
    row = sudoku.get_row(chain[2].get_coordinates()[0])
    for i in NINE_RANGE:
        if value in row[i].get_candidates() and row[i].get_coordinates()[1]!= chain[2].get_coordinates()[1]:
            chain.append(row[i])
    if len(chain) == 2:
        return False,chain
    return True, chain   

def check_Same_Block_Rows(b:Tuple[int,int],y:Tuple[int,int]) ->bool:
    if b[1]==0 and y[1]!=0 and y[1]!=1 and y[1]!=2:
        return True 
    elif b[1]==0 and y[1]!=0 and y[1]!=1 and y[1]!=2:
        return True 
    elif b[1]==0 and y[1]!=0 and y[1]!=1 and y[1]!=2:
        return True  
    elif b[1]==3 and y[1]!=3 and y[1]!=4 and y[1]!=5:
        return True  
    elif b[1]==3 and y[1]!=3 and y[1]!=4 and y[1]!=5:
        return True 
    elif b[1]==3 and y[1]!=3 and y[1]!=4 and y[1]!=5:
        return True  
    elif b[1]==6 and y[1]!=6 and y[1]!=7 and y[1]!=8:
        return True  
    elif b[1]==6 and y[1]!=6 and y[1]!=7 and y[1]!=8:
        return True  
    elif b[1]==6 and y[1]!=6 and y[1]!=7 and y[1]!=8:
        return True 
    return False     
                    
def find_chain_16(sudoku:Sudoku,field:Field,value:int) -> Tuple[bool,List[Field]]:  
    chain: List[Field] = list()
    block = sudoku.get_block(Sudoku.get_block_nr(field.get_coordinates()[0],field.get_coordinates()[1]))
    chain.append(field)
    for i in NINE_RANGE:
        if value in block[i].get_candidates() and block[i].get_coordinates()[0] != field.get_coordinates()[0]:
            chain.append(block[i])
    if len(chain)>=3:
        return False, chain
    if len(chain) < 2:
        return True, None
    col = sudoku.get_column(chain[1].get_coordinates()[1])
    for i in NINE_RANGE:
        if value in col[i].get_candidates() and col[i].get_coordinates()[0]!= chain[1].get_coordinates()[0] and col[i].get_coordinates()[0]!= chain[0].get_coordinates()[0]:
            chain.append(col[i])
    if len(chain) < 3 or len(chain) > 3:
            return True, None
    row = sudoku.get_row(chain[2].get_coordinates()[0])
    for i in NINE_RANGE:
        if value in row[i].get_candidates() and row[i].get_coordinates()[1]!= chain[2].get_coordinates()[1]:
            chain.append(row[i])
    if len(chain) == 2:
        return False,chain
    return True, chain          

def find_chain_16_1(sudoku:Sudoku,field:Field,value:int) -> Tuple[bool,List[Field]]:  
    chain: List[Field] = list()
    col = sudoku.get_column(field.get_coordinates()[1])
    chain.append(field)
    for i in NINE_RANGE:
        if value in col[i].get_candidates() and col[i].get_coordinates()[0] != field.get_coordinates()[0]:
            chain.append(col[i])
    if len(chain) > 1:
        return True,chain
    return False,None
        
def intersection_of_units(a_type: UnitType, a_nr: int, b_type: UnitType, b_nr: int) -> List[Tuple[int, int]]:
    """
    Creates the intersection of the two given units
    :returns: Coordinates of the fields in the intersection
    """
    a = get_unit(a_type, a_nr)
    b = get_unit(b_type, b_nr)

    intersection: List[Tuple[int, int]] = list()
    for coords in a:
        if coords in b:
            intersection.append(coords)
    return intersection

def get_common_units(fields: List[Tuple[int, int]]) -> List[Tuple[UnitType, int]]:
    """
    Get the units all fields have in common
    :param fields: the coordinates of the fields
    :returns: A List of all common units, sorted by unit type
    """
    common: List[Tuple[UnitType, int]] = []

    # row
    row: int = fields[0][0]
    same = True
    for i in range(1, len(fields)):
        if fields[i][0] != row:
            same = False
            break
    if same:
        common.append((UnitType.ROW, row))
    
    # column
    col: int = fields[0][1]
    same = True
    for i in range(1, len(fields)):
        if fields[i][1] != col:
            same = False
            break
    if same:
        common.append((UnitType.COLUMN, col))

    # Block
    blk = Sudoku.get_block_nr(fields[0][0], fields[0][1])
    same = True
    for i in range(1, len(fields)):
        if Sudoku.get_block_nr(fields[0][0], fields[0][1]) != blk:
            same = False
            break
    if same:
        common.append((UnitType.BLOCK, blk))

    return common
