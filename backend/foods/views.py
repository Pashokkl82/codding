from rest_framework import generics, status
from rest_framework.response import Response
from .models import *
from .serializers import *


class ListFoodView(generics.ListAPIView):
    """
    Представление создающее Электронное меню для ресторана

    """

    serializer_class = FoodSzr

    def get_queryset(self):
        return Food.objects.filter(
            category_id__is_publish=True
        ).order_by('category_id')