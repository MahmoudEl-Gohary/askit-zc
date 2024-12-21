from users.models import User
from .models import Questions, upVotes, downVotes
from .forms import QuestionsForm
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .serializers import QuestionSerializer
from users.serializers import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def question_list(request):
    questions = Questions.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def question_list_profile(request, id):
    questions = Questions.objects.filter(created_by=id)
    user = User.objects.get(pk=id)
    question_serializer = QuestionSerializer(questions, many=True)
    user_serializer = UserSerializer(user)
    return JsonResponse({
        'user': user_serializer.data,
        'questions': question_serializer.data
    }, safe=False)

@api_view(['POST'])
def question_create(request):
    form = QuestionsForm(request.data)
    if form.is_valid():
        question = form.save(commit=False)
        question.created_by = request.user
        question.save()
        serializer = QuestionSerializer(question)
        return JsonResponse(serializer.data, safe=False)
    else:
        return JsonResponse({'error': 'Invalid data'})


@api_view(['POST'])
def question_upvote(request, id):
    question = Questions.objects.get(pk=id)
    if not question.upVotes.filter(created_by=request.user):

        upvotes_obj = upVotes.objects.create(created_by=request.user)
        question = Questions.objects.get(pk=id)
        question.upvotes_count += 1
        question.upVotes.add(upvotes_obj)
        question.save()
        return JsonResponse({'message': 'Upvoted'})
    else:
        return JsonResponse({'message': 'Already Upvoted'})


@api_view(['POST'])
def question_downvote(request, id):
    question = Questions.objects.get(pk=id)
    if not question.downVotes.filter(created_by=request.user):
        downvote_obj = downVotes.objects.create(created_by=request.user)
        question.downvotes_count += 1
        question.downVotes.add(downvote_obj)
        question.save()
        return JsonResponse({'message': 'Downvoted'})
    else:
        return JsonResponse({'message': 'Already Downvoted'})

