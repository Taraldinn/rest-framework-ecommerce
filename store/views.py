# Create your views here.
from django.shortcuts import get_object_or_404, render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProductFilter
from .models import Product, Collection, Review, Cart
from .pagination import DefaultPagination
from .seriaalizers import ProductSerializer, CollectionSerializer, ReviewSerializer, CartSerializer
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import CreateModelMixin


def home(request):
    return render(request, 'index.html')


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_class = ProductFilter
    search_fields = ['title', 'description']
    ordering_fields = ['price', 'last-update']

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
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}


class CartViewSet(CreateModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
