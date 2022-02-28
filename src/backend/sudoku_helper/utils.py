from typing import List, Optional
from sudoku.base import NINE_RANGE
from sudoku.base import Sudoku, Field
from django.http import HttpRequest
from typing import Tuple, Optional

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
def sudoku_simple_check(sudoku: Sudoku) -> Tuple[bool, Optional[str]]:
    """
    Performs the simple checks on the sudoku (per row, per column, per block)
    """

    # Correct number range
    for y in NINE_RANGE:
        for x in NINE_RANGE:
            value = sudoku.get_field(y, x).get_value()
            if not (value is None or (value <= 9 and value >= 1)):
                return (False, f'The Value in [{y}, {x}] ([Row, Column]) is outside of (1, 9) (value = {value})!')


    # No double numbers
    for x in NINE_RANGE:
        [row, column, block] = [sudoku.get_row(x), sudoku.get_column(x), sudoku.get_block(x)]
        for i in range(1,9):
            if not ((row.count(i) <= 1) and (column.count(i) <= 1) and (block.count(i) <= 1)):
                return (False, f'The Value {value} occurs multiple times in a row, a column or a block°!')
    
    # correct
    return (True, None)