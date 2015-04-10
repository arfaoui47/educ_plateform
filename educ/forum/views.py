from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .serializer import *

# Create your views here.


class Forum(TemplateView):
    template_name = 'forum/forum.html'

    def get_context_data(self, **kwargs):
        context = super(Forum, self).get_context_data(**kwargs)
        return context


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


class ForumPostList(generics.ListCreateAPIView):
    model = ForumPost
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ForumPostDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ForumPost
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ForumCommentList(generics.ListCreateAPIView):
    model = ForumComment
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class ForumCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    model = ForumComment
    queryset = ForumComment.objects.all()
    serializer_class = ForumCommentSerializer
    permission_classes = [
        permissions.AllowAny
    ]

