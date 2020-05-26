from django.contrib import admin, messages

from asana_models.Instances import Instances


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
