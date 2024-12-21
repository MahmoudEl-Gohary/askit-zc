import uuid 
from django.db import models
from users.models import User
from django.utils.timesince import timesince

class Questions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100)
    body = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,related_name='Questions' ,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-created_at']
        
    def created_at_formated(self):
        return timesince(self.created_at)
    