from django.urls import path
from .views import (HomeView, checkout, ItemDetailView,product)

app_name = 'jeans'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', checkout, name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
]
