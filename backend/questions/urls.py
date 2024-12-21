from django.urls import path
from . import api

urlpatterns = [
    path('', api.question_list, name='question_list'),
    path('create/', api.question_create, name='question_create'),
]