from contextlib import nullcontext
import json
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render


from django.core import serializers

from django.views.decorators.csrf import csrf_exempt


from userdetail.models import Cart, ItemDetail, Order

# Create your views here.
# item = ItemDetail(request.POST, received_json_data)
# item.save()

@csrf_exempt
def get_item_details(request):
    if request.method == 'GET':
        item_details = ItemDetail.objects.all()
        item_details_list = serializers.serialize('json', item_details)
        return HttpResponse(item_details_list, content_type="text/json-comment-filtered")
    elif request.method == 'POST':
        received_json_data = json.loads(request.body)
        img_path = received_json_data.get('img_path')
        item_name = received_json_data.get('item_name')
        item_description = received_json_data.get('item_description')
        pices_available = received_json_data.get('pices_available')
        unit_price = received_json_data.get('unit_price')
        time_to_cook = received_json_data.get('time_to_cook')
        print(img_path, item_name, item_description,
              pices_available, unit_price, time_to_cook)
        item_obj = ItemDetail(
            img_path=img_path, item_name=item_name, item_description=item_description, pices_available=pices_available, unit_price=unit_price, time_to_cook=time_to_cook)
        item_obj.save()
        return StreamingHttpResponse('it was post request: '+str(received_json_data))
       


def get_cart(request):
    cart_items = Cart.objects.all()
    cart_items_list = serializers.serialize('json', cart_items)
    return HttpResponse(cart_items_list, content_type="text/json-comment-filtered")


def get_order(request):
    order_details = Order.objects.all()
    order_details_list = serializers.serialize('json', order_details)
    return HttpResponse(order_details_list, content_type="text/json-comment-filtered")
