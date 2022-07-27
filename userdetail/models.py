from django.db import models

# Create your models here.


class Cart(models.Model):
    img_path = models.CharField()
    item_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    unit_price = models.IntegerField()
