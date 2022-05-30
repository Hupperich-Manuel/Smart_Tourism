from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, User

admin.site.register(Question)
