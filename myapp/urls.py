# myapp/urls.py

from django.urls import path
from .views import item_list
from .views import form_input
from .views import loginPage
from .views import signUp
from .views import dashboard,login_view  
from .views import create_task_view, task_list_view,edit_task_view,delete_task_view,home_view,create_signUp


urlpatterns = [
    path('',home_view,name='home_view'),
    path('form/', form_input, name='form'),
    path('login_view/',login_view, name='login_view'),
    path('login/',loginPage, name='login'),
    path('signup/',signUp, name='signUp'),
    path('create_signUp/',create_signUp, name='create_signUp'),
    path('dashboard/',dashboard ,name='dashboard'),

    

    #TASK CRUD 
    path('create_task_view/',create_task_view,name='create_task_view'),
    path('task_list_view/',task_list_view,name='task_list_view'),
    path('task_list_view/<int:task_id>/', edit_task_view, name='edit_task_view'),
    path('delete_list_view/<int:task_id>/',delete_task_view, name='delete_task_view')

    
    
]

