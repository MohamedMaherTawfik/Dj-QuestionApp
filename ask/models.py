from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    title=models.CharField(max_length=20,default='')
    author=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,related_name='question_user')
    question=models.TextField(max_length=500)
    tags = TaggableManager()
    created_at=models.DateTimeField(default=timezone.now)
    draft=models.BooleanField(default=True)

    def __str__(self):
        return str(self.title)