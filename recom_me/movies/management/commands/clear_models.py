from django.core.management.base import BaseCommand
from movies.models import Movie, Actor, Writer, Director, Gener

class Command(BaseCommand):
    def handle(self, *args, **options):
        Movie.objects.all().delete()
        Actor.objects.all().delete()
        Writer.objects.all().delete()
        Director.objects.all().delete()
        Gener.objects.all().delete()
