import csv
from django.core.management.base import BaseCommand
from movie_app.models import actor_name

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("/Users/laurencronin/Downloads/Film_Guess/prac.csv", "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                actors_in_film = actor_name(
                    name=row['Actor'],
                    poster_one=row['Poster1'],
                    poster_two=row['Poster2'],
                    poster_three=row['Poster4'],
                    poster_four=row['Poster3'],
                )
                actors_in_film.save()
