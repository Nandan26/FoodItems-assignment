from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name ='home-page'),
    path('restaurant/<int:id>', views.restaurant_view, name = 'restaurant')
]