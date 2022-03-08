from .views import *
from django.urls import path

urlpatterns = [
    path('templates', index, name='templates'),
    path('check-sudoku', check_sudoku, name='submit-sudoku'),
    path('solve-sudoku', solve_sudoku, name='solve-sudoku'),
]
