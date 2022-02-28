from typing import List, Optional
from sudoku.base import Sudoku, Field
from django.http import HttpRequest
from typing import Tuple, Optional

def get_values_from_request(request: HttpRequest) -> List[List[int]]:
    values: List[List[Optional[int]]] = list()

    for row in range(0, 9):
        values.append(list())
        for column in range(0, 9):
            value_str = request.POST[f'{row}_{column}']
            values[row].append( 
                None if value_str == '' else int(value_str)
            )

    return values


def get_amount_of_fields_with_value(val: int, lst: List[Field]) -> int:
    """
    Returns the amount of Fields with value val in the List
    """
    n = 0
    for f in lst:
        if f.get_value() == val:
            n += 1
    
    return n


def sudoku_simple_check(sudoku: Sudoku) -> Tuple[bool, Optional[str]]:
    """
    Performs the simple checks on the sudoku (per row, per column, per block)
    """
    # Correct Number range
    if not sudoku.check_field_values():
        return (False, 'A Value is outside of (1, 9)!')

    # No double numbers
    for x in range(0, 9):
        [row, column, block] = [sudoku.get_row(x), sudoku.get_column(x), sudoku.get_block(x)]
        for i in range(1,9):
            if not ((get_amount_of_fields_with_value(i, row) <= 1) and (get_amount_of_fields_with_value(i, column) <= 1) and (get_amount_of_fields_with_value(i, block) <= 1)):
                return (False, f'The Value {i} occurs multiple times in a row, a column or a block!')
    
    # correct
    return (True, None)