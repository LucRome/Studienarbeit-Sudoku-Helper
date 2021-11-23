from typing import List, Optional
from sudoku.base import NINE_RANGE
from sudoku.base import Sudoku, Field
from django.http import HttpRequest

def get_values_from_request(request: HttpRequest) -> List[List[int]]:
    values: List[List[Optional[int]]] = list()

    for row in NINE_RANGE:
        values.append(list())
        for column in NINE_RANGE:
            value_str = request.POST[f'{row}_{column}']
            values[row].append( 
                None if value_str == '' else int(value_str)
            )

    return values

# Move to sudoku class (add tests?)
def sudoku_simple_check(sudoku: Sudoku) -> bool:
    """
    Performs the simple checks on the sudoku (per row, per column, per block)
    """
    correct = True
    for x in NINE_RANGE:
        [row, column, block] = [sudoku.get_row(x), sudoku.get_column(x), sudoku.get_block(x)]
        for i in range(1,9):
            correct &= (row.count(i) <= 1) and (column.count(i) <= 1) and (block.count(i) <= 1)
        
    return correct