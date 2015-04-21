from django.db import models
from authentification.models import *


class Note(models.Model):
    note = models.IntegerField()
    professor = models.ForeignKey(Professor)
    student = models.ForeignKey(Student)
    statement = models.CharField(max_length=50)

