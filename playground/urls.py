from django.urls import path
from playground.views import say_hello

urlpatterns = [
    path('playground/', say_hello),
]