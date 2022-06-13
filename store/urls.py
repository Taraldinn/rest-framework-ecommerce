from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from . import views
from pprint import pprint
router = DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collection', views.CollectionViewSet)

urlpatterns = router.urls

