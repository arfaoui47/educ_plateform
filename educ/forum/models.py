from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Professor(User):
    cin = models.IntegerField()

class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    year = models.IntegerField()
    professor = models.ForeignKey(Professor, related_name="classrooms")

class Student(User):
    reg_number = models.IntegerField()
    classroom = models.ForeignKey(Classroom, related_name= "students")
    score = models.IntegerField(default=0)
    skills = models.TextField(blank=True)
    interest = models.TextField(blank=True)
    about = models.TextField(blank=True)
    projects = models.TextField(blank=True)

class ForumPost(models.Model):
    contents = models.TextField()
    hashtags = models.TextField()
    statment = models.BooleanField(default=False)
    student = models.ForeignKey(Student, related_name="forum_posts")
    approval = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now=False,auto_now_add=True)

class ForumComment(models.Model):
    contents = models.TextField()
    user = models.ForeignKey(User, related_name="forum_user_comments")
    profile_post = models.ForeignKey(ForumPost, related_name="forum_post_comments")
    date = models.DateTimeField(auto_now=False,auto_now_add=True)
    appreciation = models.IntegerField(default=0)




