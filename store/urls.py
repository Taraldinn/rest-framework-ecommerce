from . import views
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collection', views.CollectionViewSet)
router.register('carts', views.CartViewSet)
products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', views.ReviewViewSet, basename='products-reviews')

urlpatterns = router.urls + products_router.urls





















