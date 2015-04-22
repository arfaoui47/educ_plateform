from django.views.generic import TemplateView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import viewsets
from rest_framework import generics, permissions
from rest_framework.parsers import FormParser, MultiPartParser


class Partage(TemplateView):
    template_name = 'partage/partage.html'

    def get_context_data(self, **kwargs):
        context = super(Partage, self).get_context_data(**kwargs)
        return context


class ProfessorDocsList(viewsets.ModelViewSet):
    model = ProfessorDocs
    queryset = ProfessorDocs.objects.all()
    serializer_class = ProfessorDocsSerializer
    parser_classes = (MultiPartParser, FormParser,)

    def perform_create(self, serializer):
        serializer.save(professor=self.request.user,
                       file=self.request.data.get('datafile'))
    def pre_save(self, obj):
        obj.samplesheet = self.request.FILES.get('file')


class SubjectList(generics.ListCreateAPIView):
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [
        permissions.AllowAny
    ]

