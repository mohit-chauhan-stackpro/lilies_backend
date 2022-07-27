import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


from django.core import serializers


from userdetail.models import Cart, ItemDetail, Order

# Create your views here.


def get_item_details(request):
    if request.method == 'GET':
        item_details = ItemDetail.objects.all()
        item_details_list = serializers.serialize('json', item_details)
        return HttpResponse(item_details_list, content_type="text/json-comment-filtered")


def get_cart(request):
    cart_items = Cart.objects.all()
    cart_items_list = serializers.serialize('json', cart_items)
    return HttpResponse(cart_items_list, content_type="text/json-comment-filtered")


def get_order(request):
    order_details = Order.objects.all()
    order_details_list = serializers.serialize('json', order_details)
    return HttpResponse(order_details_list, content_type="text/json-comment-filtered")
