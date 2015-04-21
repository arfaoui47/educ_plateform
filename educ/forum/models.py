from django.db import models
from django.contrib.auth.models import User
from authentification.models import *


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


class Club(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    student = models.ForeignKey(Student)


class AdministratorDocs(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    file = models.CharField(max_length=50)
    target = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)



