from django.views.generic import TemplateView
from django.shortcuts import render
from .serializer import *
from django import forms
from rest_framework import generics, permissions
from partage.models import *
from authentification.models import *


class Partage(TemplateView):
    template_name = 'partage/partage.html'

    def get_context_data(self, **kwargs):
        context = super(Partage, self).get_context_data(**kwargs)
        return context


class file(forms.ModelForm):
    class Meta:
        model = ProfessorDocs
        fields=('name','file','year','type','classroom')
        exclude = ["professor"]


def nouveau_file(request):
    sauvegarde = False

    if request.method == "POST":
        form = file(request.POST, request.FILES)
        if form.is_valid():
            fichier = ProfessorDocs(file = request.FILES['file'])
            fichier.name = form.cleaned_data["name"]
            fichier.file = form.cleaned_data["file"]
            fichier.year = form.cleaned_data["year"]
            fichier.type = form.cleaned_data["type"]
            fichier.classroom = form.cleaned_data["classroom"]
            fichier.professor = Professor.objects.get(id=request.user.id)
            fichier.save()
            sauvegarde = True
    else:
        form = file()

    return render(request, 'partage/partage.html', locals())


class ProfessorDocsList(generics.ListCreateAPIView):
    model = ProfessorDocs
    queryset = ProfessorDocs.objects.all()
    serializer_class = ProfessorDocsSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class SubjectList(generics.ListCreateAPIView):
    model = Subject
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ProfessorDocsDetail(generics.ListCreateAPIView):
    model = ProfessorDocs
    queryset = ProfessorDocs.objects.all()
    serializer_class = ProfessorDocsSerializer
    permission_classes = [
        permissions.AllowAny
    ]