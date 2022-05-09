from typing import List, Optional
from sudoku.base import NINE_RANGE, ALL_FIELD_VALUES
from sudoku.base import Sudoku, Field, WrongFieldValueException
from validation.validation import Validation
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from typing import Tuple, Optional

def get_values_from_request(request: HttpRequest) -> List[List[int]]:
    values: List[List[Optional[int]]] = list()

    for row in NINE_RANGE:
        values.append(list())
        for column in NINE_RANGE:
            key = f'{row}_{column}'
            if key in request.POST.keys():
                value_str = request.POST[key]
                values[row].append( 
                    None if value_str == '' else int(value_str)
                )
            else:
                values[row].append(None)

    return values


def get_candidates_from_request(request: HttpRequest) -> List[List[Optional[List[int]]]]:
    all_candidates: List[List[Optional[List[int]]]] = list()
    for row in NINE_RANGE:
        all_candidates.append(list())
        for col in NINE_RANGE:
            key = f'candidates_{row}_{col}'
            if key not in request.POST.keys():
                all_candidates[row].append([])
            else:
                field_candidates: Optional[str] = request.POST[key]
                if field_candidates is None:
                    all_candidates[row].append([])
                else:
                    all_candidates[row].append(list())
                    for i in ALL_FIELD_VALUES:
                        if f'{i}' in field_candidates:
                            all_candidates[row][col].append(i)
    
    return all_candidates


def check_and_add_candidates_from_request(request: HttpRequest, sudoku: Sudoku) -> bool:
    # sudoku candidates for check
    sudoku.select_candidates()

    # list for candidates from request
    candidate_list = get_candidates_from_request(request)

    # check whether candidates from request are possible
    for row in NINE_RANGE:
        for col in NINE_RANGE:
            if candidate_list[row][col] is not None:
                field_candidates = sudoku.get_field(row, col).get_candidates()
                for i in candidate_list[row][col]:
                    if i not in field_candidates:
                        return False
                sudoku.get_field(row, col).set_candidates(candidate_list[row][col])
    return True


def get_amount_of_fields_with_value(val: int, lst: List[Field]) -> int:
    """
    Returns the amount of Fields with value val in the List
    """
    n = 0
    for f in lst:
        if f.get_value() == val:
            n += 1
    
    return n


def sudoku_simple_check(sudoku: Sudoku) -> Tuple[bool, Optional[str]]:
    """
    Performs the simple checks on the sudoku (per row, per column, per block)
    """

    # No double numbers
    for x in NINE_RANGE:
        [row, column, block] = [sudoku.get_row(x), sudoku.get_column(x), sudoku.get_block(x)]
        for i in ALL_FIELD_VALUES:
            if not ((get_amount_of_fields_with_value(i, row) <= 1) and (get_amount_of_fields_with_value(i, column) <= 1) and (get_amount_of_fields_with_value(i, block) <= 1)):
                return (False, f'The Value {i} occurs multiple times in a row, a column or a block!')
    
    # correct
    return (True, None)


def check_sudoku_view(request: HttpRequest) -> Tuple[Optional[Sudoku], Optional[HttpResponse]]:
    """
    Handles the extraction and validation of a Sudoku from a HttpRequest, also handles the responses if something is wrong
    Returns the Sudoku if everything is correct
    """

    values = get_values_from_request(request)
    
    try:
        sudoku = Sudoku(values)
        correct = True
    except WrongFieldValueException as e:
        correct, msg = False, 'Some Field Values were not in the allowed range of 1 - 9 and therefore were removed!'
        # Initialize Sudoku without wrong Field Values
        for y in NINE_RANGE:
            for x in NINE_RANGE:
                val = values[y][x]
                if val is not None and (val > 9 or val < 1):
                    values[y][x] = None
        sudoku = Sudoku(values)

    if correct and sudoku is not None:
        val = Validation(sudoku)
        correct, msg = sudoku_simple_check(sudoku)
        if correct:
            sudoku.select_candidates()
            correct,msg = val.validate(sudoku)

    if not correct:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Please enter a correct sudoku and press Validate to proceed!',
            'failed_tests': True,
            'error_msg': msg,
        }
        return None, render(request, 'pages/index.html', context)
    
    else:
        return sudoku, None