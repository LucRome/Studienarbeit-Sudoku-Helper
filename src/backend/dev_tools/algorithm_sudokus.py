

"""
The Sudokus to test each algorithm
"""

# TODO: add missing

# Sudokus (only the values)
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
    [8, None, 1, None, None, None, None, 2, 4],
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
    [5, None, None, 8, 4, 6, 7, 9, 2],
    [6, 2, 9, 7, None, 3, 8, None, 1],
]

# mapping
NAME_MAP = {
    'hidden_single': GRID,
    'open_single': GRID2,
    'naked_pair': GRID3,
    'hidden_pair': GRID4,
    'naked_three': GRID5,
    'hidden_three': GRID6,
    'naked_hidden_four': GRID7,
    'row_block_check': GRID8,
    'block_row_check': GRID9,
    'x_wing': GRID10, # TODO: acknowledge seperation in row, col
    'third_eye': GRID12,
}