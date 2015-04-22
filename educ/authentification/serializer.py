from rest_framework import serializers
from authentification.models import *


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        ordering = ['score' , 'username']
        fields = ('id', 'reg_number', 'username' ,'first_name', 'last_name' ,'score', 'classroom')


class ProfessorsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        ordering = ['username']
        fields = ('id', 'username', 'first_name', 'last_name', 'cin')


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ('id', 'class_name', 'year')

