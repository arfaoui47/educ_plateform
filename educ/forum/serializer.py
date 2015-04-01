from rest_framework import serializers

from forum.models import User, Student, ForumPost, ForumComment

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        ordering = ['score' , 'username']
        fields = ('id', 'username', 'first_name', 'last_name', 'score')


class ForumPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForumPost
        ordering = ['approval' , 'date']
        fields = ('id', 'contents', 'hashtags', 'statment', 'student', 'approval', 'date')

class ForumCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForumComment
        ordering = ['appreciation', 'date']
        fields = ('id', 'contents', 'user', 'forumpost', 'date', 'appreciation')