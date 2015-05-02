from rest_framework import serializers

from forum.models import User
from notification.models import Notification


#ToDo: Permissions


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        ordering = ['approval' , 'date']
        fields = ('id', 'contents', 'link', 'statement', 'user', 'date')

