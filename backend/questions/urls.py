from django.urls import path
from . import api

urlpatterns = [
    path('', api.question_list, name='question_list'),
    path('<uuid:id>/upVotes/', api.question_upvote, name='question_upvote'),
    path('<uuid:id>/downVotes/', api.question_downvote, name='question_downvote'),
    path('create/', api.question_create, name='question_create'),
]