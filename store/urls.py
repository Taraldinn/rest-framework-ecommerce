from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('store/', views.product_list, name='product_list'),
    path('store/<id>/', views.product_detail, name='store'),
    # path('collection/<int:id>/', views.collection_detail, name='collection-detail'),

]

