from django.db import models
from datetime import datetime as dt
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Instructor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

class Session(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, default="", on_delete=models.CASCADE)
    # date = models.DateTimeField(default=timezone.now)


