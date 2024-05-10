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