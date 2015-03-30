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
        fields = ('id', 'username', 'first_name', 'last_name', 'posts', 'score')


class ForumPostSerializer(serializers.ModelSerializer):
    student = StudentSerializer(required=False)
    def get_validation_exclusions(self):
        # Need to exclude `author` since we'll add that later based off the request
        exclusions = super(ForumPostSerializer, self).get_validation_exclusions()
        return exclusions + ['student']

    class Meta:
        model = ForumPost
        ordering = ['approval' , 'date']
        fields = ('id', 'contents', 'hashtags', 'statment', 'student', 'approval', 'date')

class Forum_CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ForumComment
        ordering = ['appreciation', 'date']
        fields = ('id', 'contents', 'user', 'profile_post', 'date', 'appreciation')