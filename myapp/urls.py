# myapp/urls.py

from django.urls import path
from .views import item_list
from .views import form_input


urlpatterns = [
    path('', item_list, name='item_list'),
    path('form/', form_input, name='form'),
]

