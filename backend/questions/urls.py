from django.urls import path
from . import api

urlpatterns = [
    path('', api.question_list, name='question_list'),
    path('profile/<uuid:id>/', api.question_list_profile, name='question_list_profile'),
    path('create/', api.question_create, name='question_create'),
    path('<uuid:id>/upVotes/', api.question_upvote, name='question_upvote'),
    path('<uuid:id>/downVotes/', api.question_downvote, name='question_downvote'),
    path('<uuid:id>/removeVote/', api.remove_vote, name='question_remove_vote'),
    path('votes/', api.get_user_votes, name='get_user_votes'),
    path('<uuid:id>/answers/', api.question_create_answer, name='question_create_answer'),
    path('<uuid:id>/', api.question_detail, name='question_detail'),
]