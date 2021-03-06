

"""
The Sudokus to test each algorithm
"""


# Sudokus (only the values)
from sudoku.base import NINE_RANGE


GRID = [
    [2, 6, None, None, None, None, None, None, None],
    [1, None, None, 8, None, None, None, None, None],
    [None, None, None, 9, 6, 2, None, None, None],
    [None, None, None, 3, None, None, 7, None, None],
    [None, None, None, None, 5, None, None, None, 8],
    [None, None, 2, 7, 4, None, None, 9, None],
    [4, None, None, None, None, None, None, 2, None],
    [7, None, 3, None, None, 6, None, None, None],
    [None, None, None, None, 3, None, None, 8, 1],
]

GRID2 = [
    [None, 5, None, None, 6, 3, None, 9, None],
    [1, None, None, None, 2, 5, None, None, None],
    [None, None, 2, None, 1, 8, None, 4, None],
    [None, None, None, None, 7, None, None, 2, None],
    [None, None, 9, 2, None, None, 6, None, None],
    [4, 2, None, 6, 5, None, 3, None, None],
    [2, None, 5, None, None, 6, 4, None, None],
    [9, None, 1, None, None, 7, None, None, None],
    [7, None, 8, None, None, 2, None, None, None],
]

GRID3 = [
    [None, None, None, 1, 3, 7, None, None, None],
    [7, None, None, 5, 9, 6, 1, 3, None],
    [None, None, 9, None, 8, None, None, 6, None],
    [None, None, 3, None, 2, None, None, None, None],
    [5, None, None, 8, None, None, 9, 2, None],
    [None, 2, None, None, 1, None, None, None, None],
    [None, None, None, None, None, None, None, None, 8],
    [8, 7, 4, None, None, None, None, None, None],
    [None, 6, 5, 3, 4, 8, None, None, None],
]

GRID4 = [
    [None, None, None, None, None, None, None, None, None],
    [4, None, None, None, 7, None, 6, None, None],
    [None, 7, None, 2, None, 4, 3, None, None],
    [None, None, None, 9, None, None, None, 8, 4],
    [None, 6, None, None, None, None, 5, 9, 2],
    [5, 9, None, None, None, None, None, None, None],
    [None, 4, None, 8, 2, None, 9, None, 1],
    [None, None, None, 1, None, None, None, None, None],
    [6, 5, 1, 7, None, None, None, None, None],
]
        
GRID5 = [
    [None, 7, None, None, None, None, 8, None, None],
    [None, 2, None, 8, None, None, 9, 5, None],
    [None, None, None, None, None, 9, 6, None, 2],
    [None, None, None, 3, None, 4, 2, 8, 9],
    [None, None, 3, 9, None, None, 1, 6, 4],
    [4, None, None, 6, 1, None, 5, None, None],
    [None, 4, None, 2, 9, 6, None, 1, 5],
    [None, None, None, None, None, None, None, 9, 6],
    [None, None, None, 5, 3, None, 4, 2, 8],
]

GRID6 = [
    [None, None, None, 7, 4, None, None, None, 8],
    [4, 9, 6, None, None, None, None, None, None],
    [None, None, None, None, 2, None, None, 4, None],
    [None, None, None, None, 5, 7, 6, None, None],
    [8, None, None, None, None, None, None, 2, 1],
    [None, None, 3, 4, None, None, None, None, None],
    [None, None, None, 3, None, None, None, None, None],
    [1, 2, 4, None, 7, None, None, 5, None],
    [None, None, None, None, None, None, 7, None, None],
]

#grid4 = [
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#   [None, None, None, None, None, None, None, None, None],
#]

GRID7 = [
    [None, None, None, 7, 1, None, 2, 5, None],
    [None, 3, 1, 6, None, None, None, None, 8],
    [None, 5, 7, 9, None, None, None, 1, None],
    [None, None, None, None, 4, None, None, None, None],
    [None, 7, None, None, 6, 2, 1, None, 5],
    [None, None, 6, None, 9, 7, 8, None, 2],
    [None, None, 9, 2, None, 1, None, 6, None],
    [None, None, None, None, 7, 9, 3, 2, 1],
    [None, None, None, None, None, 6, None, 8, 9],
]

GRID8 = [
    [1, 2, None, None, 5, 6, None, 8, None],
    [None, None, 5, 9, None, 1, None, None, 6],
    [None, None, 6, None, None, 2, 1, None, 5],
    [None, 1, 2, None, None, None, 4, None, 7],
    [None, 3, None, 1, None, None, None, None, None],
    [7, 6, 9, None, 2, None, None, 1, 3],
    [None, None, 7, None, 1, 8, None, 9, None],
    [None, None, None, 2, None, None, None, None, None],
    [None, None, None, None, 4, 3, None, 7, None],
]
        
GRID9 = [
    [None, None, None, 9, 2, 3, 1, None, None],
    [5, None, 7, None, None, None, None, 8, None],
    [2, None, 1, None, 8, None, None, None, None],
    [None, 4, None, None, None, None, 6, None, None],
    [None, None, None, None, 5, None, None, 2, None],
    [None, 1, None, None, None, None, None, None, None],
    [8, None, None, None, 7, None, None, None, None],
    [None, None, None, 6, None, None, 4, None, None],
    [None, None, None, 3, None, None, None, None, 9],
]

GRID10 = [
    [1, None, None, None, None, None, None, 8, None],
    [8, None, None, 1, None, None, None, 2, 4],
    [7, None, None, None, None, 3, 1, 5, None],
    [None, None, None, None, 4, 1, 6, 9, 2],
    [None, 9, None, 6, 7, None, 4, 1, 3],
    [4, 1, 6, 2, 3, 9, 8, 7, 5],
    [9, None, 1, None, 6, 2, 5, None, 8],
    [None, None, None, 3, None, None, 9, None, 1],
    [None, 5, None, 9, 1, None, 2, None, 7],
]

# TODO: Algorithm??   
GRID11 = [
    [9, None, None, None, None, None, None, None, 5],
    [7, None, 2, None, 1, None, 8, None, None],
    [5, None, 4, 8, None, 6, None, None, 2],
    [4, None, 7, None, 5, None, 2, None, None],
    [8, None, None, 4, None, 3, None, None, 1],
    [1, None, 3, None, 8, None, 5, None, None],
    [3, 7, None, 9, 4, 2, 1, None, 6],
    [6, None, 1, None, 7, None, 4, 2, None],
    [2, 4, None, None, None, None, None, None, 7],
]


GRID12 = [
    [None, None, 8, 6, None, None, 2, 1, 9],
    [2, None, 6, 9, None, None, 5, 3, 8],
    [9, 5, 1, 2, 3, 8, 4, 6, 7],
    [4, 8, 2, None, 9, None, 3, 7, 6],
    [None, 9, None, 4, 6, 2, 1, 8, 5],
    [1, 6, 5, 3, 8, 7, 9, 2, 4],
    [8, None, None, None, 2, 9, 6, 4, 3],
    [5, None, None, 8, 1, 6, 7, 9, 2],
    [6, 2, 9, 7, 4, 3, 8, None, 1],
]

GRID13 = [
    [None, None, None, None, 2, None, None, None, None, ],
    [3, 8, 6, None, None, None, None, 5, 2, ],
    [5, None, None, None, None, 3, None, None, None, ],
    [None, 1, None, None, None, 8, None, 9, None, ],
    [4, None, 8, 9, None, None, 6, None, 7, ],
    [2, None, 9, None, None, 4, None, None, None, ],
    [8, None, None, 7, None, None, 3, 6, None, ],
    [9, None, None, 3, None, 1, None, 4, None, ],
    [None, None, None, None, 5, None, None, None, None, ],
]

GRID14 = [
    [None, None, 2, 8, None, 5, None, None, 7, ],
    [None, 9, None, 2, 4, None, None, 5, None, ],
    [4, None, None, 9, None, None, 2, None, None, ],
    [None, None, 6, None, None, 2, None, None, 1, ],
    [None, None, None, None, 8, None, None, 2, None, ],
    [None, None, None, None, None, None, 3, None, None, ],
    [None, None, 7, None, None, 8, None, None, 5, ],
    [None, None, None, None, 9, None, None, 6, None, ],
    [1, None, None, 4, None, None, 7, None, None, ],
]

GRID15 = [
    [6, 4, None, 8, 5, 3, None, 9, None, ],
    [9, None, None, 6, 4, 1, 8, 5, None, ],
    [1, 5, 8, 7, 2, 9, 6, 4, 3, ],
    [3, 2, 5, 1, 6, 7, 9, 8, 4, ],
    [4, None, 1, 9, 8, 2, 3, None, 5, ],
    [8, 9, None, 4, 3, 5, None, 2, None, ],
    [2, None, 9, 5, 1, 8, 4, None, None, ],
    [7, 1, None, 2, 9, 4, 5, None, 8, ],
    [5, 8, 4, 3, 7, 6, 2, 1, 9, ],
]

GRID16 = [
    [None, 7, 1, 2, 5, 8, None, None, None, ],
    [None, None, None, 4, 7, 1, 2, None, None, ],
    [2, 4, 5, 3, 6, 9, 7, None, None, ],
    [None, 5, None, 9, 1, 3, 8, 2, None, ],
    [None, None, None, 5, 2, 6, None, 7, None, ],
    [None, 2, None, 8, 4, 7, None, None, 9, ],
    [9, 3, None, 1, 8, None, None, 6, 2, ],
    [None, 8, 2, None, 3, None, None, None, 7, ],
    [None, None, 4, None, 9, 2, None, None, None, ],
]

GRID17 = [
    [None, None, None, 8, 3, 5, 2, 7, None, ],
    [None, None, 7, 9, 4, None, None, 8, None, ],
    [None, 8, None, 1, 7, None, 4, 9, None, ],
    [7, None, 8, 3, 2, 4, 1, 5, None, ],
    [None, None, None, 7, None, None, None, 3, None, ],
    [3, None, None, 5, None, None, 7, 2, None, ],
    [8, 2, 4, 6, 5, 3, 9, 1, 7, ],
    [1, 7, None, 4, 9, 8, None, 6, 2, ],
    [9, None, 6, 2, 1, 7, None, 4, None, ],
]

GRID18 = [
    [None, None, None, None, 2, 9, None, 4, 1, ],
    [None, 6, None, 1, 5, 8, 7, 2, None, ],
    [2, None, 1, None, 4, 3, None, 5, None, ],
    [None, None, None, 8, 6, None, None, 7, None, ],
    [6, None, None, 9, 3, 4, None, 1, None, ],
    [3, None, None, 2, 7, None, 9, 6, None, ],
    [1, 2, 6, 3, 8, 7, None, 9, None, ],
    [None, None, 9, 5, 1, 6, 2, 3, 7, ],
    [7, 3, 5, 4, 9, 2, 1, 8, 6, ],
]

GRID19 = [
    [None, None, None, 9, 8, None, 6, None, None],
    [4, 6, None, 3, 2, None, 1, 8, 9],
    [None, 9, None, None, 1, 6, None, None, 2],
    [None, None, 3, 7, 5, 9, None, None, None],
    [None, 5, None, 2, 4, 1, 9, None, 3],
    [None, None, None, 6, 3, 8, None, 1, None],
    [7, None, None, None, None, None, None, None, 1],
    [None, None, 1, None, None, None, None, None, None],
    [None, None, None, 1, 7, 5, None, 2, 4],
]

GRID20 = [
    [7, None, 6, 9, 1, 8, 4, 3, None, ],
    [None, 1, None, None, None, 6, 9, None, 8, ],
    [None, 8, 9, None, None, 5, None, None, None, ],
    [8, None, None, None, 6, None, None, None, None, ],
    [6, None, None, None, 4, None, 5, None, None, ],
    [1, 7, None, None, 9, 3, None, 2, None, ],
    [5, 3, 7, 1, 8, 4, 2, 6, 9, ],
    [9, 6, 8, 3, 5, 2, 7, None, None, ],
    [2, 4, 1, 6, 7, 9, None, None, None, ],
]

GRID21 = [
    [None, 6, 9, None, None, 1, None, 3, None, ],
    [None, 3, 4, None, 5, None, None, 1, None, ],
    [None, 1, None, None, 3, 7, None, None, 4, ],
    [None, None, None, 3, 7, None, None, 9, None, ],
    [None, 7, 6, 1, 8, None, None, None, 5, ],
    [1, None, None, 2, 6, None, 7, None, None, ],
    [None, None, 1, 7, None, None, None, 6, None, ],
    [6, None, 7, None, None, None, None, 5, None, ],
    [4, None, None, 5, 1, 6, None, 7, None, ],
]

GRID23 = [ # Warning: Grid has no solution (only to test Algorithm)
    [1, 2, None, 5, 7, 9, None, None, None, ],
    [None, 3, 9, 2, 4, None, 5, None, 7, ],
    [5, None, 7, 6, 3, 8, 9, 2, None, ],
    [None, None, 6, 7, None, 2, None, None, None, ],
    [None, 7, 3, None, None, 1, 2, None, None, ],
    [None, 5, None, 3, None, 4, 7, None, 9, ],
    [7, None, None, None, None, None, 8, 9, 3, ],
    [None, 9, None, None, None, 3, 1, 7, 5, ],
    [3, None, 5, 9, None, 7, 6, 4, 2, ],
]

GRID24 = [
    [None, 6, None, None, None, 8, 1, 4, None, ],
    [None, 5, None, None, None, 6, 9, 8, None, ],
    [4, 8, None, None, 3, None, 6, None, 5, ],
    [None, 2, 6, None, 8, None, 3, None, 4, ],
    [None, 1, 4, 6, None, 3, 7, None, 8, ],
    [3, 7, 8, None, None, 9, 5, 6, None, ],
    [6, 4, 5, 3, None, 2, 8, None, None, ],
    [1, 9, 2, 8, 7, 5, 4, 3, 6, ],
    [8, 3, 7, None, 6, 4, 2, 5, None, ],
]

GRID25 = [
    [None, None, 4, 3, None, 2, None, 1, 8],
    [8, None, None, None, None, None, None, 7, None],
    [None, None, 3, 8, 9, None, 4, 5, None],
    [6, 2, 8, None, None, None, 5, None, 4],
    [5, 3, 9, 4, 6, 8, 1, 2, 7],
    [4, None, None, 5, 2, None, 8, 6, None],
    [None, None, None, None, 1, None, None, None, None],
    [None, None, 5, None, None, None, 7, None, 1],
    [1, None, None, 7, 8, None, None, None, None],
]

GRID26 = [[GRID25[col][row] for col in NINE_RANGE] for row in NINE_RANGE]

# warning: Grid has no solution, only to test algorithm
GRID27 = [
    [None, None, 8, None, 5, None, 4, 3, None],
    [None, None, 3, 8, 7, None, 2, None, 5],
    [None, None, None, 9, None, None, 1, 8, 7],
    [None, 2, None, None, None, 7, 9, 1, None],
    [None, None, None, 5, None, None, 6, 2, None],
    [9, None, 6, None, None, None, None, None, None],
    [4, None, None, None, None, None, 3, None, 2],
    [None, None, None, 1, 2, 6, 8, 4, None],
    [None, 8, 2, 3, 4, None, None, None, None],
]

# mapping
NAME_MAP = {
    'hidden_single': GRID,
    'open_single': GRID2,
    'open_pair': GRID3,
    'hidden_pair': GRID4,
    'open_three': GRID5,
    'hidden_three': GRID6,
    'open_four': GRID7,
    'hidden_four': GRID7,
    'row_block_check': GRID8,
    'block_row_check': GRID9,
    'x_wing_row': GRID10,
    'x_wing_col': GRID10,
    'third_eye': GRID12,
    'skyscraper': GRID13,
    'swordfish_col': GRID14,
    'swordfish_row': GRID14,
    'dragon': GRID15,
    'square_type_1': GRID16,
    'square_type_2': GRID17,
    'square_type_4': GRID18,
    'xy_wing': GRID19,
    'xyz_wing': GRID20,
    'x_chain': GRID21,
    'w_wing': GRID23,
    'steinbutt': GRID24,
    'swordfish_fin_col': GRID25,
    'swordfish_fin_row': GRID26,
    'xy_chain': GRID27,
}