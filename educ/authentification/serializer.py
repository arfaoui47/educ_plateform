from rest_framework import serializers
from authentification.models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        ordering = ['score' , 'username']
        fields = ('id', 'username', 'first_name', 'last_name', 'reg_number' ,'score')


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        ordering = ['username']
        fields = ('id', 'username', 'first_name', 'last_name', 'cin')

