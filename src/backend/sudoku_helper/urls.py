from .views import *
from django.urls import include, path

urlpatterns = [
    path('', index, name='index'),
    path('check-sudoku', check_sudoku, name='submit-sudoku'),
    path('solve-sudoku', solve_sudoku, name='solve-sudoku'),
]
