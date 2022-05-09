from .views import *
from django.urls import path

urlpatterns = [
    path('sudoku-templates', sudoku_templates, name='sudoku_templates'),
]
