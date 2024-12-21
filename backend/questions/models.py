import uuid 
from django.db import models
from users.models import User
from django.utils.timesince import timesince

class upVotes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='upVotes' ,on_delete=models.CASCADE)
    # question = models.ForeignKey('Questions',related_name='Votes' ,on_delete=models.CASCADE)
    # is_upvote = models.BooleanField(default=True)

class downVotes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='downVotes' ,on_delete=models.CASCADE)
    
class Answers(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='answers' ,on_delete=models.CASCADE)

    def created_at_formated(self):
        return timesince(self.created_at)


class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_anonymous = models.BooleanField(default=False)

    upVotes = models.ManyToManyField(upVotes, blank=True)
    downVotes = models.ManyToManyField(downVotes, blank=True)
    upvotes_count = models.IntegerField(default=0)
    downvotes_count = models.IntegerField(default=0)

    answers = models.ManyToManyField(Answers, blank=True)
    answers_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='Questions' ,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
        
    def created_at_formated(self):
        return timesince(self.created_at)
    