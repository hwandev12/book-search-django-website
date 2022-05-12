from django.urls import path
from .views import *

app_name = 'book'

urlpatterns = [
    path('', home, name='home'),
    path('<int:pk>/details', bookDetails, name='details'),
    path('<int:pk>/shop-item', shopDetails, name='shop_details'),
    path('<int:pk>/checkout/', checkoutBookView, name='checkout'),
    path('book-lists/', login_required_book_lists, name='books'),
    path('profile/', profile, name='users-profile'),
    path("<int:pk>/update/", userProfileUpdateView, name='update_user'),
    path('user-lists/', UserListView.as_view(), name='user_lists'),
    path("create/", CreateUserView.as_view(), name='create_user'),
]
