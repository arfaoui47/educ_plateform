from django.db import models
from authentification.models import *


class Calendar(models.Model):
    contents = models.TextField()
    datebegin = models.DateTimeField(auto_now=False,auto_now_add=False)
    dateend = models.DateTimeField(auto_now=False,auto_now_add=False)
    professor = models.ForeignKey(Professor)
    student = models.ForeignKey(Student)
    classroom = models.ForeignKey(Classroom)
    club = models.CharField(max_length = 50)