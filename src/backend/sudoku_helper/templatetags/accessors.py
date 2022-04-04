from django import template
from sudoku.base import Sudoku, Field
from typing import Union, Tuple, List, Dict


register = template.Library()

"""
To access a sudoku field:
{{sudoku|row:y|column:x}}
"""
@register.filter(name='row')
def row(sudoku: Sudoku, row: int) -> Tuple[Sudoku, int]:
    return sudoku, row

@register.filter(name='column')
def column(sudoku_row: Tuple[Sudoku, int], column: int) -> Field:
    sudoku, row = sudoku_row
    return sudoku.get_field(row=row, column=column)

"""
To get values from a dictionary
Or an array or ...
"""

@register.filter(name='get_value')
def get_value(container: Union[Dict, List], idx: Union[str, int]):
    return container[idx]

