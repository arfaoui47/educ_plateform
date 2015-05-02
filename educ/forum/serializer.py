from rest_framework import serializers
from forum.models import *


#ToDo: Permissions


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