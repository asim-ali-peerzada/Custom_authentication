from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'role', 'is_staff', 'is_active', 'date_joined')
    list_filter = ('is_staff', 'is_active', 'role')
    search_fields = ('email',)
    ordering = ('-date_joined',)
    filter_horizontal = ()

admin.site.register(CustomUser, CustomUserAdmin)