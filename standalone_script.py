import os
import django
from django.conf import settings

# This is a plain python script that loads and sets up django before mucking about
# with the database using the ORM. You can also use this approach to use the templating
# system or whatever part of django you want. You would use this by running:
# python standalone_script.py
# just like any normal python script.

### NOTE!
# This is only for standalone scripts

# Setup django BEFORE you start importing your models
# Two options, either set DJANGO_SETTINGS_MODULE:
os.environ["DJANGO_SETTINGS_MODULE"] = "django_restaurant.settings"
# or call configure:
# settings.configure(DEBUG=True)
# if you're calling configure to use the ORM, you'd need to give it the DB configuration

# Next call django.setup()
django.setup()


# Now you have django, so you can import models and do stuff as normal
from restaurant.models import Dish

if Dish.objects.count() < 1:
    print("DB is empty!")

for dish in Dish.objects.all():
    print(f'{dish.id} - {dish.title}')
