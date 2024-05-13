from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """custom_command for django management

    Run this by going to the top level at the CLI and saying:
    ./manage.py custom_command

    ./manage.py custom_command --help will show the text in `help` below as well
    as all of the arguments. You can set up arguments using argparse
    
    """
    help = "Super simple command"

    def handle(self, *args, **options):
        print("You've run a custom management command!")
