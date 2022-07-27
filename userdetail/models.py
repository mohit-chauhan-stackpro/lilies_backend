from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ItemDetail(models.Model):
    img_path = models.CharField()
    item_name = models.CharField(max_length=30)
    item_description = models.TextField(max_length=200)
    pices_available = models.IntegerField()
    unit_price = models.IntegerField()
    time_to_cook = models.CharField()


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    food_item = models.ForeignKey(ItemDetail, on_delete=models.SET_NULL)
    quantity = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    img_path = models.CharField()
    order_id = models.CharField(max_length=12)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.CharField()
