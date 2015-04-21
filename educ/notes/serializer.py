from rest_framework import serializers
from notes.models import *


class NoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        ordering = ['date']
        fields = ('id', 'note', 'professor', 'student', 'statement')

