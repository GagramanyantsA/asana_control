from django.core.management.commands.runserver import BaseRunserverCommand

from django.conf import settings


class Command(BaseRunserverCommand):

    def add_arguments(self, parser):
        parser.add_argument('--asana_token', dest='asana_token', help='specify asana token key')
        super(Command, self).add_arguments(parser)

    def handle(self, *args, **options):
        asana_token = options.get('asana_token', None)

        if asana_token is None:
            raise Exception('asana_token parameter not specified')

        settings.ASANA_TOKEN = asana_token
        super(Command, self).handle(*args, **options)
