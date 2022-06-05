# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .seriaalizers import ProductSerializer


def home(request):
    return render(request, 'index.html')


@api_view()
def product_list(request):
    product= Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)
