from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .serializer import *

# Create your views here.


class Notes(TemplateView):
    template_name = 'notes/notes.html'

    def get_context_data(self, **kwargs):
        context = super(Notes, self).get_context_data(**kwargs)
        return context


class NotesList(generics.ListCreateAPIView):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class NotesDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Note
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [
        permissions.AllowAny
    ]