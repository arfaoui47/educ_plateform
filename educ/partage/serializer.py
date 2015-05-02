from rest_framework import serializers

from partage.models import *
from authentification.models import *


#ToDo: Permissions


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        ordering = ['score' , 'username']
        fields = ('id', 'username', 'first_name', 'last_name', 'score')


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('id', 'username', 'cin')


class ProfessorDocsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfessorDocs
        fields = ('name', 'file', 'year', 'type', 'professor', 'classroom')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'classroom', 'professor')