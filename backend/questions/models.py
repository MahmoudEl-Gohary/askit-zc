import uuid 
from django.db import models
from users.models import User
from django.utils.timesince import timesince

class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    upvotes_count = models.IntegerField(default=0)
    downvotes_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='questions', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']

    def created_at_formated(self):
        return timesince(self.created_at)


class UpVote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Questions, related_name='upvotes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)


class DownVote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    question = models.ForeignKey(Questions, related_name='downvotes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='downvotes', on_delete=models.CASCADE)
