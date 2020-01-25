from django.db import models
from datetime import datetime as dt
from django.utils import timezone


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

class Instructor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Session(models.Model):
    title = models.CharField(max_length=255)
    instructor = models.ForeignKey(Instructor, default="", on_delete=models.CASCADE)
    # date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

