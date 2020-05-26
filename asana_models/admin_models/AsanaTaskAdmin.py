from django.contrib import admin, messages

from asana_models.Instances import Instances


class AsanaTaskAdmin(admin.ModelAdmin):
    fields = ('project', 'description', 'user')
    list_display = ('id', 'project', 'description', 'user')
    list_filter = ('project', 'user')

    def save_model(self, request, obj, form, change):
        asana_api = Instances.asana_api()

        if change:
            if 'project' in form.changed_data:
                messages.set_level(request, messages.WARNING)
                self.message_user(request, f'Error! Project field cannot be changed!', messages.ERROR)
                return

            err = asana_api.update_task(obj.id, obj.description, obj.user_id)

            if err:
                messages.set_level(request, messages.ERROR)
                self.message_user(request, f'Error! Task {obj.id} NOT changed! Error: {err}', messages.ERROR)
                return

        else:
            task_id, err = asana_api.create_task(obj.project_id, obj.description, obj.user_id)

            if task_id is None:
                messages.set_level(request, messages.ERROR)
                self.message_user(request, f'Error! New task NOT added! Error: {err}', messages.ERROR)
                return

            obj.id = task_id

        super(AsanaTaskAdmin, self).save_model(request, obj, form, change)
