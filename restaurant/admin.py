from django.contrib import admin

from restaurant.models import Dish, UploadedFile

# Register your models here.
admin.site.register(Dish)
admin.site.register(UploadedFile)

