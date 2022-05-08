from django.shortcuts import render
from store.models import Product
# Create your views here.


def say_hello(request):
    """say hello function"""
    product = Product.objects.filter(price__gt(20))
    print(product)

    return render(request, 'index.html', {'name': 'Fardin','products':list(product)})
