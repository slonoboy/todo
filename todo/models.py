from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=500)
    pub_date = models.DateTimeField('date created', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isDone = models.BooleanField(default=False)
    done_date = models.DateTimeField('date done', blank=True, default=None, null=True)
    