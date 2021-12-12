from django.contrib import admin
from .models import Task, Collection


class TaskInLineAdmin(admin.TabularInline):
    model = Task


class CollectionAdmin(admin.ModelAdmin):
    inlines = [TaskInLineAdmin]


admin.site.register(Collection, CollectionAdmin)
