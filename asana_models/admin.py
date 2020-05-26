from django.contrib import admin
from asana_models.models import AsanaUser, AsanaTask, AsanaProject
from asana_models.admin_models import AsanaProjectAdmin, AsanaUserAdmin, AsanaTaskAdmin

admin.site.register(AsanaProject, AsanaProjectAdmin)
admin.site.register(AsanaUser, AsanaUserAdmin)
admin.site.register(AsanaTask, AsanaTaskAdmin)
