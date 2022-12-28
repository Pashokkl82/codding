from rest_framework import serializers
from .models import *


class fdSzr(serializers.ModelSerializer):
    """
        Сериализатор категории блюд
    """
    class Meta:
        model = FoodCategory
        fields = (
            'name',
            'is_publish'
        )

class ToppingSzr(serializers.ModelSerializer):
    """
        Сериализатор ингридиента
    """
    class Meta:
        model = Topping
        fields = (
            'name'
        )

class FoodSzr(serializers.ModelSerializer):
    """
        Сериализатор Блюда
    """

    categories = fdSzr(many=True)
    toppings = ToppingSzr(many=True)
    class Meta:
        model = Food
        fields = (
            'name',
            'description',
            'price',
            'is_vegan',
            'is_special',
            'toppings',
            'categories'
        )

class ToppingSzr(serializers.ModelSerializer):
    """
        Сериализатор ингридиента
    """
    class Meta:
        model = Topping
        fields = (
            'name'
        )

