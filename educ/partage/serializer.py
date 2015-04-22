from rest_framework import serializers

from partage.models import *
from authentification.models import *

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
    professor = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id'
    )
    class Meta:
        model = ProfessorDocs
        ordering = ['appreciation', 'date']
        fields = ('id', 'name', 'file', 'year', 'type', 'subject', 'professor', 'date')


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ('id', 'name', 'classroom', 'professor')