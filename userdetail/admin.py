from django.contrib import admin

# Register your models here.
from .models import ItemDetail, Order, Cart

admin.site.register(ItemDetail)
admin.site.register(Order)
admin.site.register(Cart)
