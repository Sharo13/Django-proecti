from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Dish, Category

def dish_list(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()

    category_filter = request.GET.get('category')
    if category_filter:
        dishes = dishes.filter(category__name=category_filter)

    nutty_filter = request.GET.get('nutty')
    if nutty_filter:
        dishes = dishes.filter(is_nutty=True)

    vegetarian_filter = request.GET.get('vegetarian')
    if vegetarian_filter:
        dishes = dishes.filter(is_vegetarian=True)

    price_min = request.GET.get('price_min')
    price_max = request.GET.get('price_max')
    if price_min:
        dishes = dishes.filter(price__gte=price_min)
    if price_max:
        dishes = dishes.filter(price__lte=price_max)

    spicy_min = request.GET.get('spicy_min')
    spicy_max = request.GET.get('spicy_max')
    if spicy_min:
        dishes = dishes.filter(spicy_level__gte=spicy_min)
    if spicy_max:
        dishes = dishes.filter(spicy_level__lte=spicy_max)

    context = {
        'categories': categories,
        'dishes': dishes,
    }
    return render(request, 'menu/dish_list.html', context)

def dish_details(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    context = {
        'dish': dish
    }
    return render(request, 'menu/dish_details.html', context)

def add_to_cart(request, dish_id):
    dish = get_object_or_404(Dish, id=dish_id)
    cart = request.session.get('cart', {})
    
    if str(dish_id) in cart:
        cart[str(dish_id)]['quantity'] += 1
    else:
        cart[str(dish_id)] = {
            'name': dish.name,
            'price': str(dish.price),
            'quantity': 1
        }

    cart_count = request.session.get('cart_count', 0)
    cart_count += 1
    request.session['cart_count'] = cart_count

    request.session['cart'] = cart
    return redirect('dish_list')


def reset_cart(request):
    request.session['cart_count'] = 0
    return redirect('dish_list')
