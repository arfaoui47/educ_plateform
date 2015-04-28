from django.db import models
from authentification.models import *
from django import forms

class ProfessorDocs(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/')
    year = models.IntegerField()
    type = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom)
    professor = models.ForeignKey(Professor)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class Subject(models.Model):
    name = models.CharField(max_length=50)
    classroom = models.ForeignKey(Classroom)
    professor = models.ForeignKey(Professor)