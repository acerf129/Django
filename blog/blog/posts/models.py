from django.db import models
from datetime import datetime
# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=100000)
    create_Date = models.DateTimeField(default=datetime.now,blank=True)