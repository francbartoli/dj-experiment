from dj_experiment.models import Catalog
from django.core.management.base import BaseCommand, CommandError
from humanfriendly.tables import format_pretty_table


class Command(BaseCommand):
    """Retrieve information about experiments from the catalog."""

    help = 'Retrieve information about experiments from the catalog'

    def add_arguments(self, parser):
        """Add arguments for handling the command."""
        pass

    def handle(self, *args, **options):
        """Query all the entries from the catalog model."""
        if args:
            raise CommandError("infocatalog takes no arguments")
        column_names = ['Catalog Name']
        # [self.stdout.write(cat, ending='') for cat in Catalog.objects.all()]
        catalog = [cat.title for cat in Catalog.objects.all()]

        self.stdout.write(format_pretty_table(
            [catalog, ], column_names))
