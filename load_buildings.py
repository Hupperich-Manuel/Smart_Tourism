from polls.models import Buildings
import csv
from django.utils import timezone

def run():
    with open('data/places.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Buildings.objects.all().delete()

        for row in reader:
            print(row)

            film = Buildings(name=row[0],
                            question_text1=row[1],
                            question_text1=row[2],
                            question_text3=row[3],
                            pub_date=timezone.now()
                            )
            film.save()
