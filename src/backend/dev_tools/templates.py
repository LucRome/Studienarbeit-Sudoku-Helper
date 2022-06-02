from typing import List
from sudoku.base import Sudoku

class SudokuTemplate:
    count: int = 0
    nr: int
    title: str
    sudoku: Sudoku

    def __init__(self, title: str, values: List[List[int]]) -> None:
        self.nr = SudokuTemplate.count
        SudokuTemplate.count += 1
        self.title = title
        self.sudoku = Sudoku(values=values)


TEMPLATES: List[SudokuTemplate] = [
    SudokuTemplate(
        title="Valid",
        values=[
            #0      1       2       3       4       5       6       7       8    
            [None, 5, None, None, 3, 2, 4, 9, None],
            [None, 9, 6, None, None, None, 2, 1, None],
            [None, 8, None, 1, None, 6, 7, None, 3],
            [None, None, None, None, 6, None, 3, 7, None],
            [None, 6, None, None, None, 9, 1, None, 5],
            [None, 1, None, 3, 7, None, None, 6, None],
            [None, None, None, None, None, None, 5, 3, None],
            [8, 3, None, 2, 5, 7, None, 4, None],
            [5, None, None, 6, None, 3, 8, None, 7],
        ]
    ),
    SudokuTemplate(
        title='easy',
        values=[
            [6, None, 9, None, 2, 8, None, None, None],
            [None, 8, 2, None, None, None, 4, None, 9],
            [None, None, None, 9, None, 5, None, None, 8],
            [None, None, None, None, 3, None, None, None, None],
            [7, 5, 3, 2, 8, 4, None, None, None],
            [None, None, None, None, 5, None, 3, 7, None],
            [None, None, 6, None, None, None, None, None, 3],
            [4, None, 8, None, None, 3, 5, None, None],
            [3, 1, None, 8, 9, None, None, None, 7],
        ]
    )
]