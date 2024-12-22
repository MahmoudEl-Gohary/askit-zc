from rest_framework import serializers
from .models import Questions, Answers
from users.serializers import UserSerializer

class QuestionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Questions
        fields = ('id', 'title', 'body', 'created_at_formated', 'created_by', 'is_anonymous', 'upvotes_count', 'downvotes_count')
        

class AnswersSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Answers
        fields = ('id', 'body', 'created_at', 'created_by')


class QuestionDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    answers = AnswersSerializer(read_only=True,many=True)
    class Meta:
        model = Questions
        fields = ('id', 'title', 'body', 'upvotes_count', 'downvotes_count', 'created_at_formated', 'created_by', 'is_anonymous', 'answers')