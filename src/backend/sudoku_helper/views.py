from django.http.request import HttpRequest
from django.shortcuts import render

from sudoku.base import Sudoku

# Create your views here.
def index(request: HttpRequest):
    sudoku = Sudoku()
    r = range(0,9)
    context={
        'sudoku': sudoku,
        'range': r
    }
    return render(request, 'index.html', context)
    