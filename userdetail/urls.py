from django.urls import path
from . import views

urlpatterns = [
    path('itemdetails/', views.get_item_details, name="itemdetails"),
    path('cart/', views.get_cart, name="cart"),
    path('order/', views.get_order, name="order"),
    path('register/', views.post_register, name="register"),
    path('login/', views.check_if_register, name="login"),
]
