from django.forms import ModelForm
from .models import Questions

class QuestionsForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['title', 'body', 'is_anonymous']