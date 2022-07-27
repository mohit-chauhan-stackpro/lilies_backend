from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ItemDetail(models.Model):
    img_path = models.ImageField()
    item_name = models.CharField(max_length=30)
    item_description = models.TextField(max_length=200)
    pices_available = models.IntegerField()
    unit_price = models.IntegerField()
    time_to_cook = models.CharField(max_length=30)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_item = models.ManyToManyField(ItemDetail)
    quantity = models.IntegerField()


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img_path = models.ImageField()
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.CharField(max_length=30)
