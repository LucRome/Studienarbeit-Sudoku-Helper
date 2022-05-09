from django.http import Http404
from django.shortcuts import render
from django.http.request import HttpRequest
from django.conf import settings

from .templates import TEMPLATES
from sudoku.base import NINE_RANGE


# Create your views here.
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


