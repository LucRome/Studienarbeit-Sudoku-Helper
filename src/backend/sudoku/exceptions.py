"""
Contains exceptions
"""

class WrongFieldValueException(Exception):
    def __init__(self, val: int):
        self.message = f"Error: Field Value {val} is too high or low.\nAllowed are numbers 1 - 9"

class WrongFieldCandidateException(Exception):
    def __init__(self, val: int):
        self.message = f"Error: Candidate Value {val} is too high or low.\nAllowed are numbers 1 - 9"

class OutOfFieldsException(Exception):
    def __init__(self):
        self.message = f"Error: Out of the Sudoku Field.\nColumns, Rows and Blocks are Indexed with 0 - 8."