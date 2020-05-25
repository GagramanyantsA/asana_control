from django.contrib import admin
from asana_models.models import AsanaUser, AsanaTask, AsanaProject


# Register your models here.

@admin.register(AsanaUser)
class AsanaUserAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')


@admin.register(AsanaProject)
class AsanaProjectAdmin(admin.ModelAdmin):
    fields = ('project_name',)
    list_display = ('id', 'project_name')


@admin.register(AsanaTask)
class AsanaTaskAdmin(admin.ModelAdmin):
    fields = ('project', 'description', 'user')
    list_display = ('id', 'project', 'description', 'user')
    list_filter = ('project', 'user')
