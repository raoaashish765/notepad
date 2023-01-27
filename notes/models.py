from asyncio.windows_events import NULL
from django.db import models

# Create your models here.

class Allnotes(models.Model):
    link=models.CharField(max_length=20, default=NULL)
    pass1=models.CharField(max_length=20, default=NULL)

    def __str__(self):
        return self.link

class Txtall(models.Model):
    link=models.CharField(max_length=20, default=NULL)
    usrtxt=models.TextField(max_length=100000, default=NULL)

    def __str__(self):
        return self.link