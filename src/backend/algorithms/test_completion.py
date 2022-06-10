import unittest as ut
from algorithms.algorithms import *
from sudoku.base import Field, Sudoku
from validation.validation import Validation
from sudoku_helper.utils import sudoku_simple_check
from dev_tools.algorithm_sudokus import NAME_MAP
import json

def nxt_step(sudoku: Sudoku) -> Tuple[bool, Optional[str], Optional[Dict[str, Any]]]:
    """
    True + None + Dict if one algorithm is used, else false + msg + None
    """
    if not verify(sudoku):
        return False, 'Sudoku has no solution', None
    solver = Algorithm(sudoku)
    for alg in solver.get_name_fn_dict().values():
        success, dict = alg()
        if success:
            print('.', end='')
            return True, None, dict
    return False, 'No Algorithm was able to solve it', None

def try_to_solve(sudoku: Sudoku) -> Tuple[bool, str]:
    """
    True if Sudoku is solvable with algorithms
    """
    all_returns: List[Dict[str, Any]] = []
    str_new, str_old = '',''
    while not sudoku.is_solved():
        success, msg, dict = nxt_step(sudoku)
        if not success:
            return False, msg
        # check for repetition
        str_new = json.dumps(dict)
        if str_new == str_old:
            return False, f"The same action occured twice -> maybe problem with algorithm: {dict['algorithm']}"
        all_returns.append(dict)
        str_old = str_new

    print('solved')
    return True, ''

def verify(sudoku: Sudoku) -> bool:
    """
    Verifies the sudoku
    """
    success, msg = sudoku_simple_check(sudoku)
    if not success:
        return False
    success, msg = Validation(sudoku).validate(sudoku)
    return success


class TestCompleteSolvability(ut.TestCase):
    """
    Tests whether the Algorithms are able to solve the given sudokus
    (Sudokus from: https://sudoku.com/de (mittel, experte, höllisch))
    """

    def __test_sudokus(self, sudokus: List[Sudoku]):
        """
        Perform test operations for every sudoku in the List
        """
        successfull, total = 0, 0
        for sudoku in sudokus:
            sudoku.select_candidates()

            if not verify(sudoku):
                print(f'sudoku {total} has no solution -> not Tested')
            else:
                success, msg = try_to_solve(sudoku)
                total += 1
                if success:
                    successfull += 1
                else:
                    print(f'Error: sudoku {total}: {msg}')
        print(f'\n\nSolved: {successfull}/{total}')
        self.assertGreater(successfull/total, 0.5, msg='not even half of the sudokus could be solved')

    def test_middle(self):
        """
        Test mediocre sudokus (Expert Level on Website)
        """
        sudokus = [
            Sudoku([
                [None, None, 4, None, None, 1, None, None, 8],
                [None, None, None, None, None, None, None, None, 7],
                [3, None, None, 4, None, None, None, None, None],
                [1, None, None, 2, None, 6, None, None, 9],
                [None, None, None, None, 3, 8, 7, None, None],
                [None, 2, None, None, None, None, None, 1, None],
                [None, 8, None, 3, None, None, None, 2, None],
                [None, 6, None, None, 1, None, None, None, None],
                [None, 7, None, None, None, None, None, 6, 5],
            ]),
            Sudoku([
                [None, None, None, None, 1, None, None, None, None],
                [2, None, None, None, 3, None, None, 9, None],
                [3, None, 1, None, None, 4, None, None, None],
                [None, 8, None, 7, None, 5, None, None, None],
                [None, None, 4, None, None, None, None, 5, None],
                [None, 9, None, None, None, None, None, None, 2],
                [None, None, None, 6, None, None, 4, None, None],
                [None, None, None, None, None, None, 3, 2, 1],
                [None, None, None, 4, 8, None, 9, None, None],
            ]),
            
        ]

        self.__test_sudokus(sudokus)


    def test_hard(self):
        """
        Test hard sudokus (hell level on Website)
        """
        sudokus = [
            Sudoku([
                [None, None, 1, None, None, None, None, None, 7],
                [None, 9, None, None, None, 6, 1, 3, None],
                [None, None, None, 3, None, None, None, None, 4],
                [None, 6, None, None, 2, None, None, None, None],
                [None, None, None, None, None, None, None, None, 1],
                [None, None, 9, 7, None, None, 5, 8, None],
                [None, None, 5, 8, None, None, 3, 9, None],
                [8, None, None, None, None, 7, None, None, None],
                [None, None, None, None, None, None, None, 4, None],
            ]),
            Sudoku([
                [None, None, None, 3, None, None, None, None, None],
                [8, None, None, None, None, None, None, None, 6],
                [None, None, 5, None, 1, 9, 4, None, None],
                [None, None, None, None, None, 2, None, None, None],
                [None, None, 1, None, 7, 5, 9, None, None],
                [None, 9, None, None, None, None, None, 4, None],
                [None, None, None, 2, None, None, 7, None, None],
                [None, None, 3, 4, None, None, None, None, None],
                [5, None, None, None, 3, 7, None, 8, None],
            ]),
            Sudoku([
                [None, None, 6, None, 3, None, None, 5, 2],
                [None, 1, None, None, None, 7, None, None, None],
                [None, None, None, None, None, None, 4, None, None],
                [None, None, 2, None, 5, None, None, 8, 3],
                [None, None, None, None, None, None, None, None, 9],
                [6, None, None, 2, None, None, None, None, None],
                [None, None, 8, None, None, None, 9, None, None],
                [None, None, None, None, 4, None, 6, None, None],
                [7, None, None, None, None, 3, None, 4, 8],
            ])
        ]

        self.__test_sudokus(sudokus)

    def test_algorithm_sudokus(self):
        successfull, total = 0, 0
        for key, values in NAME_MAP.items():
            sudoku = Sudoku(values)
            sudoku.select_candidates()

            if not verify(sudoku):
                print(f'sudoku {key} has no solution -> not Tested')
            else:
                success, msg = try_to_solve(sudoku)
                total += 1
                if success:
                    successfull += 1
                else:
                    print(f'Error: sudoku {key}: {msg}')
        print(f'\n\nSolved: {successfull}/{total}')
        self.assertGreater(successfull/total, 0.5, msg='not even half of the sudokus could be solved')
