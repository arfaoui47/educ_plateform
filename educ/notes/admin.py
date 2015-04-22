from django.contrib import admin
from notes.models import *


class NoteAdmin(admin.ModelAdmin):

    ordering       = ('statement', )
    list_display   = ('student', 'professor', 'note')
    list_filter    = ('statement','student','professor')


admin.site.register(Note, NoteAdmin)
