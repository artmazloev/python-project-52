
# Register your models here.
from django.contrib import admin

from task_manager.tasks.models import Task, TaskLabel


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'author', 'executor', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    list_filter = ('status', 'author', 'executor', 'created_at')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'status')
        }),
        ('Участники', {
            'fields': ('author', 'executor')
        }),
        ('Системная информация', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )


@admin.register(TaskLabel)
class TaskLabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'label')
    list_display_links = ('id',)
    list_filter = ('task', 'label')
    search_fields = ('task__name', 'label__name')
