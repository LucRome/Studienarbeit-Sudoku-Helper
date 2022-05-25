from .views import *
from django.urls import path

urlpatterns = [
    path('sudoku-templates', sudoku_templates, name='sudoku_templates'),
    path('', home, name='dev_tools_home'),
    path('test_algorithm/<str:name>', test_single_algorithm, name='test_single_algorithm')
]
