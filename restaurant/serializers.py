from rest_framework import serializers

from restaurant.models import Dish, UploadedFile

class DishSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dish
        fields = ['id', 'title', 'cuisine_type', 'category', 'description', 'price', 'spicy_level']
    

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadedFile
        fields = ['file', 'uploaded']
