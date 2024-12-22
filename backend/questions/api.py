from users.models import User
from .models import Questions, UpVote, DownVote, Answers
from .forms import QuestionsForm
from django.shortcuts import render
from django.http import JsonResponse
from .serializers import QuestionSerializer, AnswersSerializer, QuestionDetailSerializer
from users.serializers import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def question_list(request):
    questions = Questions.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return JsonResponse(serializer.data, safe=False)


@api_view(['GET'])
def question_list_profile(request, id):
    try:
        user = User.objects.get(pk=id)
        if request.user.id == user.id:
            questions = Questions.objects.filter(created_by=user)
        else:
            questions = Questions.objects.filter(created_by=user, is_anonymous=False)
        question_serializer = QuestionSerializer(questions, many=True)
        user_serializer = UserSerializer(user)
        return JsonResponse({
            'user': user_serializer.data,
            'questions': question_serializer.data,
        }, safe=False)
    except User.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)


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
    try:
        question = Questions.objects.get(pk=id)

        if UpVote.objects.filter(question=question, created_by=request.user).exists():
            return JsonResponse({'message': 'Already Upvoted'})

        DownVote.objects.filter(question=question, created_by=request.user).delete()

        UpVote.objects.create(question=question, created_by=request.user)
        question.upvotes_count = UpVote.objects.filter(question=question).count()
        question.downvotes_count = DownVote.objects.filter(question=question).count()
        question.save()

        return JsonResponse({'message': 'Upvoted'})
    except Questions.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)

@api_view(['POST'])
def question_downvote(request, id):
    try:
        question = Questions.objects.get(pk=id)

        if DownVote.objects.filter(question=question, created_by=request.user).exists():
            return JsonResponse({'message': 'Already Downvoted'})

        UpVote.objects.filter(question=question, created_by=request.user).delete()

        DownVote.objects.create(question=question, created_by=request.user)
        question.downvotes_count = DownVote.objects.filter(question=question).count()
        question.upvotes_count = UpVote.objects.filter(question=question).count()
        question.save()

        return JsonResponse({'message': 'Downvoted'})
    except Questions.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)


@api_view(['POST'])
def remove_vote(request, id):
    try:
        question = Questions.objects.get(pk=id)

        if UpVote.objects.filter(question=question, created_by=request.user).exists():
            UpVote.objects.filter(question=question, created_by=request.user).delete()

        elif DownVote.objects.filter(question=question, created_by=request.user).exists():
            DownVote.objects.filter(question=question, created_by=request.user).delete()

        question.upvotes_count = UpVote.objects.filter(question=question).count()
        question.downvotes_count = DownVote.objects.filter(question=question).count()
        question.save()

        return JsonResponse({'message': 'Vote removed'})
    except Questions.DoesNotExist:
        return JsonResponse({'error': 'Question not found'}, status=404)

@api_view(['GET'])
def get_user_votes(request):
    votes = []

    upvotes = UpVote.objects.filter(created_by=request.user)
    for upvote in upvotes:
        votes.append({'question_id': upvote.question.id, 'type': 'upvote'})

    downvotes = DownVote.objects.filter(created_by=request.user)
    for downvote in downvotes:
        votes.append({'question_id': downvote.question.id, 'type': 'downvote'})

    return JsonResponse(votes, safe=False)


@api_view(['GET'])
def question_detail(request, id):
    question_obj = Questions.objects.get(pk=id)


    return JsonResponse({
        'question': QuestionDetailSerializer(question_obj).data
    })


@api_view(['POST'])
def question_create_answer(request, id):

    answer = Answers.objects.create(body=request.data['body'], created_by=request.user)
    question = Questions.objects.get(pk=id)
    question.answers.add(answer)
    question.answers_count += 1
    question.save()

    serializer = AnswersSerializer(answer)


    return JsonResponse(serializer.data, safe=False)