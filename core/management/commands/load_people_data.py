from django.core.management.base import BaseCommand

from core.models import People


class Command(BaseCommand):

    help = 'Load people data from CSV file'

    def handle(self, *args, **kwargs):
        pass
