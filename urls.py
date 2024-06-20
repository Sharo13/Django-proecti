from django.urls import path
from .views import dish_list, dish_details, add_to_cart,reset_cart

urlpatterns = [
    path('', dish_list, name='dish_list'),
    path('dish_details/<int:dish_id>/', dish_details, name='dish_details'),
    path('add_to_cart/<int:dish_id>/', add_to_cart, name='add_to_cart'),
    path('reset_cart/', reset_cart, name='reset_cart'),
]

