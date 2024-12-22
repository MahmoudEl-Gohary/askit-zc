from rest_framework import serializers
from .models import Questions
from users.serializers import UserSerializer

class QuestionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    class Meta:
        model = Questions
        fields = ('id', 'title', 'body', 'created_at_formated', 'created_by', 'is_anonymous', 'upvotes_count', 'downvotes_count')