from django.urls import path
from . import views
urlpatterns = [
    path('store/',views.product_list ),
    path('store/<int:pk>/', views.product_detail, name='store'),
    path('play/', views.just_orm)
]