from rest_framework import serializers

from forum.models import User, Student, Professor, Calendar
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


class CalenderSerliazer(serializers.ModelSerializer):

    class Meta:
        model = Calendar
        fields = ('contents','datebegin','dateend','professor','student','classroom','club')
