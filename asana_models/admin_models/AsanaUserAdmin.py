from django.contrib import admin, messages

from asana_models.Instances import Instances


class AsanaUserAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('id', 'name')

    def save_model(self, request, obj, form, change):
        if change:
            messages.set_level(request, messages.WARNING)
            self.message_user(request, 'Change operation prevented for Asana Users!', messages.WARNING)
            return

        user_id, err = Instances.asana_api().create_user(obj.name)

        if user_id is None:
            messages.set_level(request, messages.ERROR)
            self.message_user(request, f'Error! New project NOT added! Error: {err}', messages.ERROR)
            return

        obj.id = user_id

        super(AsanaUserAdmin, self).save_model(request, obj, form, change)
