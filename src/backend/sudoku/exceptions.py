"""
Contains exceptions
"""

class WrongFieldValueExcetion(Exception):
    def __init__(self, val: int):
        self.message = f"Error: Field Value {val} is too high or low.\nAllowed are numbers 0 - 9"

class WrongFieldCandidateException(Exception):
    def __init__(self, val: int):
        self.message = f"Error: Candidate Value {val} is too high or low.\nAllowed are numbers 0 - 9"