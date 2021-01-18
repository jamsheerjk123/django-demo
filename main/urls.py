from  django.urls import path
from main import views
from .models import ProductModel
urlpatterns=[
    path('index/',views.home),
    path('table/',views.pro),
    path('create_data/',views.create_product)
   
]