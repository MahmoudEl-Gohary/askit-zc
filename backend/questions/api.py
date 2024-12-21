from users.models import User
from .models import Questions
from .forms import QuestionsForm
from django.shortcuts import render
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
    
