from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from django.contrib.auth.decorators import user_passes_test
from .serializer import *
from rest_framework import generics, permissions


class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
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


def superuser_required(*args, **kwargs):
    return user_passes_test(lambda u: u.is_superuser, login_url='admin:login')(*args, **kwargs)



def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login_student.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        # if hasattr(user, 'cin'):
        #     request.session['user_type'] = "professor"
        # else:
        #     request.session['user_type'] = "student"
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return  HttpResponseRedirect('/accounts/login')

def loggedin(request):
    return render_to_response('forum/index.html',
        {'user' : request.user})

def invalid_login(request):
    return render_to_response('login_student.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')


