# often used in django views
# from django.shortcuts import render

from django.http import JsonResponse

# restframework approach
from rest_framework import permissions, viewsets

from .serializers import DishSerializer
from .models import Dish

# Create your views here.
def dishview(request):
    """a traditional django view to handle the 'GET' method

    We don't get anything for free like we do with DRF. Could possibly switch 
    this to a class based view and get a bit more
    """
    dishlist = Dish.objects.all()

    dish_dict_list = [{'title': d.title, 
                       'cuisine_type': d.cuisine_type,
                       'category': d.category,
                       'description': d.description,
                       'price': d.price,
                       'spicy_level': d.spicy_level
                       } for d in dishlist]

    return JsonResponse(dish_dict_list, safe=False)


# We will be creating viewsets instead
class DishViewSet(viewsets.ModelViewSet):
    """Viewset for handling Dish CRUD

    Uncomment permission_classes for authentication
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    # permission_classes = [permissions.IsAuthenticated]


class RandomDishViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for random dishes
    """
    queryset = Dish.random_objects.all()
    serializer_class = DishSerializer
