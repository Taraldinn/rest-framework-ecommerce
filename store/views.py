# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product
from store.seriaalizers import ProductSerializer


@api_view()
def product_list(request):
    return Response("ok")


@api_view()
def product_detail(request,id):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializer(product)
    return Response(serializer.data)



def just_orm(request):
    products = Product.objects.all()

    return render(request, "index.html", {"products": products})