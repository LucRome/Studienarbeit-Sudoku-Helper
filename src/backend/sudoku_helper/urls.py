from .views import *
from django.urls import path

urlpatterns = [
    path('', index, name='index'),
    path('check-sudoku', check_sudoku, name='submit-sudoku'),
]
