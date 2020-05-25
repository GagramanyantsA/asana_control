from django.contrib import admin, messages

from django.conf import settings

from asana_models.AsanaApi import AsanaApi
from asana_models.models import AsanaUser, AsanaTask, AsanaProject


class Instances:
    __asana_api = None

    @staticmethod
    def asana_api():
        if Instances.__asana_api is None:
            Instances.__asana_api = AsanaApi(settings.ASANA_TOKEN)

        return Instances.__asana_api


@admin.register(AsanaUser)
class AsanaUserAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if change:
            messages.set_level(request, messages.WARNING)
            self.message_user(request, 'Change operation prevented for Asana Users!', messages.WARNING)
            return

        asana_api = Instances.asana_api()
        user_id, err = asana_api.create_user(obj.name)

        if user_id is None:
            messages.set_level(request, messages.ERROR)
            self.message_user(request, f'Error! New project NOT added! Error: {err}', messages.ERROR)
            return

        obj.id = user_id

        super(AsanaUserAdmin, self).save_model(request, obj, form, change)


@admin.register(AsanaProject)
class AsanaProjectAdmin(admin.ModelAdmin):
    fields = ('project_name',)
    list_display = ('id', 'project_name')

    def save_model(self, request, obj, form, change):
        asana_api = Instances.asana_api()

        if change:
            err = asana_api.update_project(obj.id, obj.project_name)

            if err:
                messages.set_level(request, messages.ERROR)
                self.message_user(request, f'Error! Project {obj.id} NOT changed! Error: {err}', messages.ERROR)
                return

        else:
            project_id, err = asana_api.create_project(obj.project_name)

            if project_id is None:
                messages.set_level(request, messages.ERROR)
                self.message_user(request, f'Error! New project NOT added! Error: {err}', messages.ERROR)
                return

            obj.id = project_id

        super(AsanaProjectAdmin, self).save_model(request, obj, form, change)


@admin.register(AsanaTask)
class AsanaTaskAdmin(admin.ModelAdmin):
    fields = ('project', 'description', 'user')
    list_display = ('id', 'project', 'description', 'user')
    list_filter = ('project', 'user')

    # todo add & update task
