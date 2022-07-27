from django.db import models

# Create your models here.


class Cart(models.Model):
    img_path = models.CharField()
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()


class Order(models.Model):
    img_path = models.CharField()
    order_id = models.CharField(max_length=12)
    quantity = models.IntegerField()
    total = models.IntegerField()
    status = models.CharField()


class ItemDetail(models.Model):
    img_path = models.CharField()
    item_name = models.CharField(max_length=30)
    item_description = models.TextField(max_length=200)
    pices_available = models.IntegerField()
    unit_price = models.IntegerField()
    time_to_cook = models.CharField()
