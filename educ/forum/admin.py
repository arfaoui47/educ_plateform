from django.contrib import admin
from forum.models import *


admin.site.register(ForumPost)
admin.site.register(ForumComment)