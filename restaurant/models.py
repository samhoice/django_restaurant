from random import sample 
from django.db import models
from django.conf import settings

from logging import getLogger

logger = getLogger(settings.LOGGER_NAME)

# Create your models here.
MEAL_CATEGORIES = {
        "BR": "Breakfast",
        "LU": "Lunch",
        "DI": "Dinner",
        "BH": "Brunch",
        "AP": "Appetizer",
        }


class RandomDishManager(models.Manager):
    def get_queryset(self):
        """There's a bug here in that model managers get cached.
        """
        logger.info("Random Dish Manager")
        base_queryset = super().get_queryset().all()
        pks = list(base_queryset.values_list('pk', flat=True))
        sample_size = 5 if len(pks) > 5 else len(pks)
        random_pks = sample(pks, k=sample_size)
        return base_queryset.filter(id__in=random_pks)


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

    # first save the default manager
    objects = models.Manager()

    # now add a new manager that overrides get_queryset
    random_objects = RandomDishManager()


class Restaurant(models.Model):
    name = models.CharField(max_length=256)


class Menu(models.Model):
    title = models.CharField(max_length=256)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish)

class UploadedFile(models.Model):
    file = models.FileField()
    uploaded = models.DateTimeField(auto_now_add=True)


