from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_completed', 'is_deleted', 'created_at']
    list_filter = ['is_completed', 'is_deleted']
