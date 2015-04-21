from django.db import models
from django.contrib.auth.models import User


class Professor(User):
    cin = models.IntegerField()


class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    year = models.IntegerField()


class Student(User):
    reg_number = models.IntegerField()
    classroom = models.ForeignKey(Classroom)
    score = models.IntegerField(default=0)
    skills = models.TextField(blank=True)
    interest = models.TextField(blank=True)
    about = models.TextField(blank=True)
    projects = models.TextField(blank=True)