
# Register your models here.
from django.contrib import admin

from task_manager.labels.models import Label


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
