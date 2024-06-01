from django.core.files import File
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

# restframework approach
from rest_framework import permissions, status, viewsets, views
from rest_framework.decorators import api_view
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .serializers import DishSerializer, FileUploadSerializer
from .models import Dish, UploadedFile

from logging import getLogger

logger = getLogger(settings.LOGGER_NAME)

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
    permission_classes = [permissions.IsAuthenticated]


class RandomDishViewSet(viewsets.ReadOnlyModelViewSet):
    """Viewset for random dishes
    """
    queryset = Dish.random_objects.all()
    serializer_class = DishSerializer


class FileUploadAPIView(views.APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):

        logger.info("FileUpload - Post")

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            logger.info("Serializer is_valid")
            # you can access the file like this from serializer
            # uploaded_file = serializer.validated_data["file"]
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        else:
            logger.error("The serializer is NOT valid")
            logger.error("serializer error: %s", serializer.errors)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

# @csrf_exempt
@api_view(["GET",])
def getFile(request):

    file_id = request.query_params['file_id']

    uploaded = get_object_or_404(UploadedFile, pk=file_id)
    filepath = settings.MEDIA_ROOT / uploaded.file.name

    logger.warning(f"Request for file at: {filepath}")

    buffer = None
    with open(filepath, 'rb') as image_file:
        # image_file = File.open(filepath, 'r')
        buffer = image_file.read()

    return HttpResponse(buffer, content_type="image/jpg")
