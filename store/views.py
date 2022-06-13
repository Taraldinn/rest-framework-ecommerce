# Create your views here.
from django.db.models import Count
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Collection, Review
from .seriaalizers import ProductSerializer, CollectionSerializer, ReviewSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


def home(request):
    return render(request, 'index.html')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()[:20]
    serializer_class = ProductSerializer

    def get_serializer_contex(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        if OrderItems.objects.filter(product_id=kwargs['pk']).count() > 0:
            return Response({"message": "Cannot delete a product that is in an order"},
                            status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, *args, **kwargs)


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

























