from django.db import models
import uuid
from django.db import models


class FoodCategory(models.Model):
    """
    Модель категория блюда
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Наименовние категории',
                            blank=False)
    is_publish = models.BooleanField()

    class Meta:
        verbose_name = 'Категрия блюда'
        verbose_name_plural = 'Категория блюд'
        db_table = 'fd_db'

    def __str__(self):
        return self.name


class Topping(models.Model):
    """
    Модель ингредиент
    """
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Наименовние ингредиента',
                            blank=False)

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        db_table = 'topping_db'

    def __str__(self):
        return self.name


class Food(models.Model):
    """
    Модель блюдо
    """
    category_id = models.ForeignKey(FoodCategory, on_delete=models.DO_NOTHING, null=True, default=None)
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=255,
                            verbose_name='Название блюда',
                            blank=False)
    description = models.CharField(max_length=255,
                            verbose_name='описание блюда',
                            blank=False)
    price = models.IntegerField()
    is_vegan = models.BooleanField(default=True)
    is_special = models.BooleanField(default=True)
    toppings = models.ForeignKey(Topping, on_delete=models.DO_NOTHING, null=True, default=None)

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
        db_table = 'food_db'

    def __str__(self):
        return '%s -> %s' % (self.name, self.uuid)
