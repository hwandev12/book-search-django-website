from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/details', bookDetails, name='details'),
    path('<int:pk>/shop-item', shopDetails, name='shop_details')
]
