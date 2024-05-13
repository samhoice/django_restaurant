from django.db import models

# Create your models here.
MEAL_CATEGORIES = {
        "BR": "Breakfast",
        "LU": "Lunch",
        "DI": "Dinner",
        "BH": "Brunch",
        "AP": "Appetizer",
        }


class Dish(models.Model):
    """A dish from a restaurant

    Note that we haven't defined "id" here. ID will automatically be added if
    you don't define one of your fields as a primary key. If you use the auto
    primary key, pk and id are synonyms.
    """

    title = models.CharField(max_length=256)
    cuisine_type = models.CharField(max_length=256)
    category = models.CharField(max_length=3, choices=MEAL_CATEGORIES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    spicy_level = models.PositiveSmallIntegerField()


class Restaurant(models.Model):
    name = models.CharField(max_length=256)


class Menu(models.Model):
    title = models.CharField(max_length=256)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)
