from django.conf import settings

from asana_models.AsanaApi import AsanaApi


class Instances:
    __asana_api = None

    @staticmethod
    def asana_api():
        if Instances.__asana_api is None:
            Instances.__asana_api = AsanaApi(settings.ASANA_TOKEN)

        return Instances.__asana_api
