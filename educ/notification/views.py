from django.views.generic import TemplateView
from rest_framework import generics, permissions
from .serializer import *


class Notifications(TemplateView):
    template_name = 'notification/notification.html'

    def get_context_data(self, **kwargs):
        context = super(Notifications, self).get_context_data(**kwargs)
        return context


class UserList(generics.ListCreateAPIView):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class NotificationList(generics.ListCreateAPIView):
    model = Notification
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    model = Notification
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [
        permissions.AllowAny
    ]





