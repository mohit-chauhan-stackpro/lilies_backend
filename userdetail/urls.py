from ssl import VERIFY_ALLOW_PROXY_CERTS
from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('itemdetails/', views.get_item_details, name="itemdetails"),
    path('cart/', views.get_cart, name="cart"),
    path('order/', views.get_order, name="order"),
    path('register/', views.register_user, name="register"),
    path('login/', views.check_if_register, name="login"),
    path('itemdetail/<int:pk>', views.get_item_detail, name="itemdetail"),
    path('addorder', views.add_order, name="addorder")
]
