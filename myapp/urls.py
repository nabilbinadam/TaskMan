# myapp/urls.py

from django.urls import path
from .views import item_list
from .views import form_input
from .views import loginPage
from .views import signUp
from .views import dashboard    
from .views import create_task_view, task_list_view


urlpatterns = [
    path('', item_list, name='item_list'),
    path('form/', form_input, name='form'),
    path('login/',loginPage, name='login'),
    path('signup/',signUp, name='signUp'),
    path('dashboard/',dashboard ,name='dashboard'),
    path('create_task_view/',create_task_view,name='create_task_view'),
    path('task_list_view/',task_list_view,name='task_list_view'),
]

