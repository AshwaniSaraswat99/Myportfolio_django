from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import contact, Project

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(contact)
admin.site.register(Project)
