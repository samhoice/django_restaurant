from rest_framework import serializers

from restaurant.models import Dish

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['title', 'cuisine_type', 'category', 'description', 'price', 'spicy_level']
