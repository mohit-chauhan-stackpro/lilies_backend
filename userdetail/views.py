from contextlib import nullcontext
from email.policy import HTTP
import json
from re import I
from django.http import HttpResponse, JsonResponse, StreamingHttpResponse
from django.shortcuts import render


from django.core import serializers

from django.views.decorators.csrf import csrf_exempt


from userdetail.models import Cart, CartItem, ItemDetail, Order, OrderItem

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
import jwt


# Create your views here.


@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        username = received_json_data.get('username')
        email = received_json_data.get('email')
        password = received_json_data.get('password')
        print(username, email, password)
        User.objects.create_user(username, email, password)
        return HttpResponse('User Register Successfully!!')
    return HttpResponse('Wrong Request')


@csrf_exempt
def check_if_register(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        # payload_data = received_json_data
        my_secret = 'my_super_secret'
        username = received_json_data.get('username')
        password = received_json_data.get('password')
        id = User.objects.get(username=username).pk
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return HttpResponse('Not Allowed to login!')
        else:
            token = jwt.encode(payload={
                "id": id,
                "username": username,
                "password": password
            }, key=my_secret)
            print(token)
            return HttpResponse(json.dumps(token))
    return HttpResponse('Wrong Request')


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
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        print(token)

        payload = jwt.decode(token, "my_super_secret", algorithms=["HS256"])
        print(payload)
        id = payload.get('id')
        cart = Cart.objects.filter(user__id=id).last()
        cart_items = CartItem.objects.filter(cart=cart)

        response_data = {
            "cart_id": cart.id,
            "items": []
        }

        for cart_item in cart_items:
            response_data["items"].append(
                {"id": cart_item.food_item.id, "food_item": cart_item.food_item.item_name, "qunatity": cart_item.quantity})

        return JsonResponse(response_data)
        # cart_items = Cart.objects.filter(user=id)
        # cart_items_list = serializers.serialize('json', cart_items)
        # return HttpResponse(cart_items_list, content_type="text/json-comment-filtered")


@csrf_exempt
def add_to_cart(request):
    received_json_data = json.loads(request.body)
    token = request.headers.get('Authorization')
    print(token)
    payload = jwt.decode(token, "my_super_secret", algorithms=["HS256"])
    print(payload)
    id = payload.get('id')
    cart_items = received_json_data.get('food_items')
    print(cart_items)

    return HttpResponse('added to cart Successfully')


def get_order(request):
    if request.method == 'GET':
        token = request.headers.get('Authorization')
        print(token)
        payload = jwt.decode(token, "my_super_secret", algorithms=["HS256"])
        print(payload)
        id = payload.get('id')
        order = Order.objects.filter(user__id=id).last()
        order_items = OrderItem.objects.filter(order=order)
        response_data = {
            "order_id": order.id,
            "items": []
        }
        for order_item in order_items:
            response_data["items"].append(
                {"id": order_item.food_item.id, "food_item": order_item.food_item.item_name, "qunatity": order_item.quantity})
        return JsonResponse(response_data)

        # order_details = Order.objects.filter(user=id)
        # order_details_list = serializers.serialize('json', order_details)
        # return HttpResponse(order_details_list, content_type="text/json-comment-filtered")


@csrf_exempt
def add_order(request):
    received_json_data = json.loads(request.body)
    token = request.headers.get('Authorization')
    print(token)
    payload = jwt.decode(token, "my_super_secret", algorithms=["HS256"])
    print(payload)
    id = payload.get('id')
    order_items = received_json_data.get('food_items')
    print(order_items)

    return HttpResponse('order added Successfully')


# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6OCwidXNlcm5hbWUiOiJzb251IiwicGFzc3dvcmQiOiJzb251QDEyMyJ9.56VwdeYLUioR-8CNeE7ZXkM4MoftF2RrGo4ffAUAHTk

def get_item_detail(request, pk):
    item_detail = ItemDetail.objects.filter(pk=pk)
    item_detail_list = serializers.serialize('json', item_detail)
    return HttpResponse(item_detail_list, content_type="text/json-comment-filtered")
