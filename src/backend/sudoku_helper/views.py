from re import S
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from sudoku.base import NINE_RANGE
from validation.validation import *

from sudoku.exceptions import WrongFieldValueException

from .utils import get_values_from_request, sudoku_simple_check

from sudoku.base import Sudoku

# Create your views here.
def index(request: HttpRequest):
    """
    Homepage: empty Sudoku to fill
    """
    sudoku = Sudoku()
    context={
        'sudoku': sudoku,
        'range': NINE_RANGE,
        'quickinfo': 'Welcome, please enter the numbers into the sudoku and press validate to proceed!'
    }
    return render(request, 'pages/index.html', context)

@require_http_methods(['POST'])
def check_sudoku(request: HttpRequest):
    """
    Check the submitted Sudoku (comes after index)
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
            if val.validate_sudoku(sudoku,0,0) == 1:
                correct = True
            else:
                correct = False

    if not correct:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Please enter a correct sudoku and press Validate to proceed!',
            'failed_tests': True,
            'error_msg': msg,
        }
        return render(request, 'pages/index.html', context)
    
    else:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Your sudoku was verified, now you can start solving it by pressing solve!'
        }
        return render(request, 'pages/verified.html', context)

@require_http_methods(['POST'])
def solve_sudoku(request: HttpRequest):
    """
    Apply the solving Algorithms to the Sudoku
    """
    pass
