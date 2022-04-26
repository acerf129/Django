from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=30)
    place = models.CharField(max_length=30,default='Europe')
    description = models.TextField()
    data_created = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name