from django.core.management.base import BaseCommand, CommandError

# playing with the ORM

# load the json into the DB
import json

# First import some models
from restaurant.models import Dish


class Command(BaseCommand):
    help = "Playing with models and the ORM"

    def handle(self, *args, **options):
        print("You've run a custom management command!")

        filepath = "data/foodList.json"

        with open(filepath, "r") as fp:  # fp is a pointer to a file
            food_data = json.load(fp)

        print(food_data[15])

        for item in food_data:
            dish = Dish(
                # id=item.id,
                title=item['title'],
                cuisine_type=item['cuisine_type'],
                category="DI",
                description=item['description'],
                price=item['price'],
                spicy_level=item['spicy_level'],
            )

            dish.save()
