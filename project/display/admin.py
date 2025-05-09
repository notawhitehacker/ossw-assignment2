from django.contrib import admin

from .models import *


class ProjAdmin(admin.ModelAdmin) :
    list_display = ('name', 'contents', 'githuburl', 'credit')
    ordering = ['-credit']

admin.site.register(Proj, ProjAdmin) 
