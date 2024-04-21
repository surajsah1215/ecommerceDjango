
from django.shortcuts import render
from .models import Product, Cart, Order
from .recommendation_model import recommender

def home(request):
    # Get recommended products for a specific user (for demonstration purposes, let's assume user_id=1)
    user_id = 1  # Assuming user_id=1 for demonstration purposes
    recommended_products = recommender.get_recommendations_for_user(user_id)

    
    product_list_items = []
    for product in recommended_products.itertuples(index=False):
        product_list_items.append(
            f'<li><a href="{{% url "product_detail" {product.id} %}}">{product.name}</a></li>'
        )

    context = {
        'product_list_items': product_list_items
    }
    return render(request, 'home.html', context)

def add_to_cart(request, product_id):
    # Add product to user's cart
    user_id = 1  # Assuming user_id=1 for demonstration purposes
    user_cart, created = Cart.objects.get_or_create(user_id=user_id)
    product = Product.objects.get(id=product_id)
    cart_item, created = user_cart.cartitem_set.get_or_create(product=product)
    
    return render(request, 'cart.html', {'cart': user_cart})

def checkout(request):
    # Create an order for the user's cart and clear the cart
    user_id = 1  # Assuming user_id=1 for demonstration purposes
    user_cart = Cart.objects.get(user_id=user_id)
    order = Order.objects.create(user_id=user_id, total_price=user_cart.total_price)
    order.products.set(user_cart.products.all())
    user_cart.products.clear()
    
    return render(request, 'checkout.html', {'order': order})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context)
