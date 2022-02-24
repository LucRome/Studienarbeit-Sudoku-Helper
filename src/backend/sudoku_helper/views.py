from email.policy import default
import re
from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from sudoku.base import NINE_RANGE

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
    }
    return render(request, 'pages/index.html', context)

@require_http_methods(['POST'])
def check_sudoku(request: HttpRequest):
    """
    Check the submitted Sudoku (comes after index)
    """
    values = get_values_from_request(request)
    sudoku = Sudoku(values)

    correct = sudoku_simple_check(sudoku) # TODO: please add the complex sudoku check here

    if not correct:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'failed_tests': True,
            'error_msg': 'TODO: Error Message' # TODO
        }
        return render(request, 'pages/index.html', context)
    
    else:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
        }
        return render(request, 'pages/verified.html', context)

@require_http_methods(['POST'])
def solve_sudoku(request: HttpRequest):
    """
    Apply the solving Algorithms to the Sudoku
    """
    pass