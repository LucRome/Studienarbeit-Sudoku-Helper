from django.http.request import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.conf import settings
from algorithms.algorithms import Algorithm
from sudoku.base import NINE_RANGE
from validation.validation import *

from sudoku.exceptions import WrongFieldValueException

from .utils import get_values_from_request, sudoku_simple_check, check_sudoku_view, check_and_add_candidates_from_request

from sudoku.base import Sudoku

import json

# Create your views here.
def index(request: HttpRequest):
    """
    Homepage: empty Sudoku to fill
    """
    sudoku = Sudoku()
    context={
        'sudoku': sudoku,
        'range': NINE_RANGE,
        'quickinfo': 'Willkommen, bitte geben Sie die Nummern in das Sudoku ein und drücken Sie Validieren um fortzufahren!',
        'link_dev_tools': settings.DEBUG # only link settings tools when debug config is active
    }
    return render(request, 'pages/index.html', context)

@require_http_methods(['POST'])
def check_sudoku(request: HttpRequest):
    """
    Check the submitted Sudoku (comes after index)
    """
    sudoku, response = check_sudoku_view(request)

    if response:
        return response
        
    else:
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Ihr Sudoku wurde verifiziert, jetzt können Sie beginnen es zu lösen! Drücken Sie Lösen um fortzufahren!'
        }
        return render(request, 'pages/verified.html', context)


@require_http_methods(['POST'])
def solve_sudoku(request: HttpRequest):
    """
    Apply the solving Algorithms to the Sudoku
    """
    sudoku, response = check_sudoku_view(request)

    if response:
        return response
        
    # extract and check candidates
    candidates_correct = check_and_add_candidates_from_request(request, sudoku)
    
    if not candidates_correct:
        # error with candidates -> back to index
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Bitte geben Sie ein korrektes Sudoku ein und drücken Sie Validieren um fortzufahren!',
            'failed_tests': True,
            'error_msg': 'Fehler: Die übertragenen Kandidaten können nicht stimmten.',
        }
        return render(request, 'pages/index.html', context)
    
    algorithms = Algorithm(sudoku)
    for al_fn in algorithms.get_all_algorithms():
        success, dict = al_fn()
        
        # TODO: check if algorithm brought any use (i.e. candidates were deleted)

        if success:
            context = {
                'sudoku': sudoku,
                'range': NINE_RANGE,
                'quickinfo_template': f"algorithms/quickinfos/{dict['algorithm']}.html",
                'dict': dict,
                'algo_script': f"js/algorithm_scripts/{dict['algorithm']}.js",
                'dict_str': json.dumps(dict)
            }
            return render(request, 'pages/solve.html', context)

    # TODO: Wenn nie success: Error Message


@require_http_methods(['POST'])
def compute_candidates(request: HttpRequest):
    """
    Compute the candidates for the sudoku
    (Called after each algorithm, in case a field got a value)
    """
    sudoku, response = check_sudoku_view(request)

    if response:
        return response

    candidates_correct = check_and_add_candidates_from_request(request, sudoku)
    if not candidates_correct:
        # error with candidates -> back to index
        context = {
            'sudoku': sudoku,
            'range': NINE_RANGE,
            'quickinfo': 'Bitte geben Sie ein korrektes Sudoku ein und drücken Sie Validieren um fortzufahren!',
            'failed_tests': True,
            'error_msg': 'Fehler: Die übertragenen Kandidaten können nicht stimmen!',
        }
        return render(request, 'pages/index.html', context)
    
    sudoku.recalculate_candidates()
    context = {
        'sudoku': sudoku,
        'range': NINE_RANGE,
        'quickinfo': 'Nach den Änderungen durch den letzten Algorithmus sehen das Sudoku und die Kandidaten wie folgt aus.'
    }

    return render(request, 'pages/computed_candidates.html', context)