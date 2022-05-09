from django.http import Http404, HttpResponseServerError
from django.shortcuts import render
from django.http.request import HttpRequest
from django.conf import settings

from .templates import TEMPLATES
from .algorithm_sudokus import NAME_MAP
from sudoku.base import NINE_RANGE, Sudoku
from algorithms.algorithms import Algorithm

import json


# Create your views here.
def home(request: HttpRequest):
    if not settings.DEBUG:
        raise Http404('Page not found')
    
    algorithms = NAME_MAP.keys()
    context = {
        'algorithms': algorithms
    }
    return render(request, 'dev_tools/pages/home.html', context)


def sudoku_templates(request: HttpRequest):
    """
    a list of predefined sudoku templates
    (only works in Debug mode)
    """
    if not settings.DEBUG:
        raise Http404('Page not found')
    
    context = {
        'templates': TEMPLATES,
        'range': NINE_RANGE
    }

    return render(request, 'dev_tools/pages/sudoku_template_page.html', context)


def test_single_algorithm(request: HttpRequest, name: str):
    if not settings.DEBUG:
        raise Http404('Page not found')

    # get Sudoku
    values = NAME_MAP[name]
    if values is None:
        raise Http404('Algorithm not found (no values given)')
    sudoku = Sudoku(values)
    sudoku.select_candidates()
    al = Algorithm(sudoku)
    algo_fn = al.get_name_fn_dict()[name]
    if algo_fn is None:
        raise Http404('Algorithm not found (no function given)')

    success, dict = algo_fn()
    if not success:
        raise HttpResponseServerError('Algorithm wasnt successfull')
    sudoku.recalculate_candidates()
    context = {
        'sudoku': sudoku,
        'range': NINE_RANGE,
        'quickinfo_template': f"algorithms/quickinfos/{dict['algorithm']}.html",
        'dict': dict,
        'algo_script': f"js/algorithm_scripts/{dict['algorithm']}.js",
        'dict_str': json.dumps(dict)
    }
    return render(request, 'pages/solve.html', context)
