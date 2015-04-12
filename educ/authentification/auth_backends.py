from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from django.core.exceptions import ImproperlyConfigured
from django.db.models import get_model


class StudentModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class_s.objects.get(username=username)
            if user.check_password(password):
                return user
        except self.user_class_s.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class_s.objects.get(pk=user_id)
        except self.user_class_s.DoesNotExist:
            return None

    @property
    def user_class_s(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get student model')
        return self._user_class


class ProfessorModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class_p.objects.get(username=username)
            if user.check_password(password):
                return user
        except self.user_class_p.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class_p.objects.get(pk=user_id)
        except self.user_class_p.DoesNotExist:
            return None

    @property
    def user_class_p(self):
        if not hasattr(self, '_user_class'):
            self._user_class = get_model(*settings.CUSTOM_USER_MODEL_P.split('.', 2))
            if not self._user_class:
                raise ImproperlyConfigured('Could not get student model')
        return self._user_class




