from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .serializer import *

# Create your views here.


class Calender(TemplateView):
    template_name = 'calender/calender.html'

    def get_context_data(self, **kwargs):
        context = super(Calender, self).get_context_data(**kwargs)
        return context

class EventList(generics.ListCreateAPIView):
    model = Calendar
    queryset = Calendar.objects.all()
    serializer_class = CalenderSerliazer
    permission_classes = [
        permissions.AllowAny
    ]

class StudentList(generics.ListCreateAPIView):
    model = Student
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ProfessorList(generics.ListCreateAPIView):
    model = Professor
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    permission_classes = [
        permissions.AllowAny
    ]