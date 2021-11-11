from django import template
from sudoku.base import Sudoku, Field


register = template.Library()

"""
To access a sudoku field:
{{sudoku|row:y|column:x}}
"""
@register.filter(name='row')
def row(sudoku: Sudoku, row: int) -> tuple[Sudoku, int]:
    return sudoku, row

@register.filter(name='column')
def column(sudoku_row: tuple[Sudoku, int], column: int) -> Field:
    sudoku, row = sudoku_row
    return sudoku.get_field(row=row, column=column)