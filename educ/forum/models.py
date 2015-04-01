from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Professor(User):
    cin = models.IntegerField()

class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    year = models.IntegerField()
    professor = models.ForeignKey(Professor)


class Student(User):
    reg_number = models.IntegerField()
    classroom = models.ForeignKey(Classroom)
    score = models.IntegerField(default=0)
    skills = models.TextField(blank=True)
    interest = models.TextField(blank=True)
    about = models.TextField(blank=True)
    projects = models.TextField(blank=True)


class ForumPost(models.Model):
    contents = models.TextField()
    hashtags = models.TextField()
    statment = models.BooleanField(default=False)
    student = models.ForeignKey(Student)
    approval = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class ForumComment(models.Model):
    contents = models.TextField()
    user = models.ForeignKey(User)
    forumpost = models.ForeignKey(ForumPost)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    appreciation = models.IntegerField(default=0)


class ProfilePost(models.Model):
    contents = models.TextField()
    hashtags = models.TextField()
    statment = models.CharField(max_length=50, default='public')
    student = models.ForeignKey(Student)
    approval = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class ProfileComment(models.Model):
    contents = models.TextField()
    student = models.ForeignKey(Student)
    profilepost = models.ForeignKey(ProfilePost)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class MailBox(models.Model):
    contents = models.TextField()
    sender = models.CharField(max_length=50)
    adresser = models.ForeignKey(User)
    subject = models.CharField(max_length= 50)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class Reclamation(models.Model):
    contents = models.TextField()
    sender = models.ForeignKey(User)
    subject = models.CharField(max_length= 50)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)

class Notification(models.Model):
    contents = models.TextField()
    link = models.CharField(max_length=50)
    statement = models.BooleanField(default=0)
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class Club(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    student = models.ForeignKey(Student)


class ProfessorDocs(models.Model):
    name = models.CharField(max_length=50)
    file = models.CharField(max_length=50)
    year = models.IntegerField()
    type = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    professor = models.ForeignKey(Professor)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)

class AdministratorDocs(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)


class Calendar(models.Model):
    contents = models.TextField()
    datebegin = models.DateTimeField(auto_now=False,auto_now_add=False)
    dateend = models.DateTimeField(auto_now=False,auto_now_add=False)
    professor = models.ForeignKey(Professor)
    student = models.ForeignKey(Student)
    classroom = models.ForeignKey(Classroom)
    club = models.CharField(max_length = 50)


class Note(models.Model):
    note = models.IntegerField()
    professor = models.ForeignKey(Professor)
    student = models.ForeignKey(Student)
    subject = models.CharField(max_length=50)
    statement = models.CharField(max_length=50)




