from typing import Type, Optional
from .base import NINE_RANGE, Field, Sudoku, FIELD_VALUE_MAX, FIELD_VALUE_MIN
from .exceptions import OutOfFieldsException, WrongFieldCandidateException, WrongFieldValueException
import unittest

def print_sudoku(sudoku: Sudoku):
    print("\n")
    for row in range(0,9):
        txt: str = ""
        for column in range(0,9):
            txt += sudoku.get_field(row, column).get_value().__str__()
            if column in [2, 5]:
                txt += "|"
        print(txt)
        if (row + 1) % 3 == 0:
            print(" ---------")

def field_to_value(field: Field) -> Optional[int]:
    return field.get_value()

class TestField(unittest.TestCase):
    
    def test_value(self):
        # set values
        val = 8
        field: Field = Field(coordinates=(0,0), value=val)
        self.assertEqual(val, field.get_value())
        val = 3
        field.set_value(val=val)
        self.assertEqual(val, field.get_value())
        field.remove_value()
        self.assertIsNone(field.get_value())
        field = Field(coordinates=(0,0))
        self.assertIsNone(field.get_value())

        # throw error
        with self.assertRaises(WrongFieldValueException):
            field.set_value(val=(FIELD_VALUE_MAX + 1))
        with self.assertRaises(WrongFieldValueException):
            field.set_value(val=(FIELD_VALUE_MIN - 1))

    def test_candidates(self):
        field: Field = Field(coordinates=(0,0))
        self.assertListEqual(field.get_candidates(), [])
        field.add_candidate(1)
        field.add_candidate(3)
        self.assertEqual(field.get_candidates(), [1, 3])
        field.remove_candidate(3)
        self.assertNotIn(3, field.get_candidates())

class SudokuTest(unittest.TestCase):
    def test_row(self):
        # TODO: only assign values to the row thats Tested
        values = [
            [1,2,3,4,5,6,7,8,9],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
            [1,1,1,1,1,1,1,1,1],
        ]

        sudoku: Sudoku = Sudoku(values)
        print_sudoku(sudoku)
        target_values = [1,2,3,4,5,6,7,8,9]
        row_values = list(map(field_to_value, sudoku.get_row(0)))
        self.assertEqual(row_values, target_values)
        # for i in range(0,9):
        #     self.assertEqual(target_values[i], row[i].get_value())

    def test_column(self):
        values = [
            #0 1 2 3  4  5 6 7 8
            [1,1,1,1, 9 ,1,1,1,1],
            [1,1,1,1, 8 ,1,1,1,1],
            [1,1,1,1, 7 ,1,1,1,1],
            [1,1,1,1, 6 ,1,1,1,1],
            [1,1,1,1, 5 ,1,1,1,1],
            [1,1,1,1, 4 ,1,1,1,1],
            [1,1,1,1, 3 ,1,1,1,1],
            [1,1,1,1, 2 ,1,1,1,1],
            [1,1,1,1, 1 ,1,1,1,1],
        ]

        sudoku: Sudoku = Sudoku(values)
        target_values = [9,8,7,6,5,4,3,2,1]
        column_values = list(map(field_to_value, sudoku.get_column(4)))
        self.assertListEqual(column_values, target_values)
    
    def test_block(self):
        values = [
            [1,1,1, 1,1,1, 1,1,1],
            [1,1,1, 1,1,1, 1,1,1],
            [1,1,1, 1,1,1, 1,1,1],
             
            [1,1,1, 1,1,1, 1,2,3],
            [1,1,1, 1,1,1, 4,5,6],
            [1,1,1, 1,1,1, 7,8,9],
             
            [1,1,1, 1,1,1, 1,1,1],
            [1,1,1, 1,1,1, 1,1,1],
            [1,1,1, 1,1,1, 1,1,1],
        ]
        
        sudoku: Sudoku = Sudoku(values)
        target_values = [1,2,3,4,5,6,7,8,9]
        block_values = list(map(field_to_value, sudoku.get_block(Sudoku.get_block_nr(row=4, column=7))))
        self.assertListEqual(target_values, block_values)

    def test_coordinates(self):
        sudoku = Sudoku()
        for row in NINE_RANGE:
            for col in NINE_RANGE:
                coords = (row, col)
                self.assertEqual(coords, sudoku.get_field(row, col).get_coordinates())

"""
    Candidate Select Tests
"""

class CandidateTest(unittest.TestCase):
    def test_1(self):
        values = [
            #0      1       2       3       4       5       6       7       8    
            [None,  1,      2,      3,      None,   None,   None,   None,   None],
            [None,  None,   None,   None,   None,   None,   None,   None,   None],
            [None,  None,   None,   None,   None,   None,   None,   None,   None],

            [4,     None,   None,   None,   None,   None,   None,   None,   None],
            [None,  None,   None,   None,   None,   None,   None,   None,   None],
            [None,  None,   None,   None,   None,   None,   None,   None,   None],

            [None,  None,   None,   None,   None,   None,   None,   2,      9],
            [None,  None,   None,   None,   None,   None,   1,      None,   None],
            [None,  None,   None,   None,   None,   None,   None,   3,      None],
        ]   

        sudoku = Sudoku(values)
        sudoku.select_candidates()
        self.assertListEqual(sudoku.get_field(0,0).get_candidates(), [5,6,7,8,9])
        self.assertListEqual(sudoku.get_field(0,4).get_candidates(), [4,5,6,7,8,9])
        self.assertListEqual(sudoku.get_field(8,8).get_candidates(), [4,5,6,7,8])
        

if __name__ == '__main__':
    unittest.main()