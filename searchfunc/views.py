from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.db.models import Q

def home(request):
    sliders = SliderImagesContent.objects.all()
    context = {
        'sliders': sliders
    }
    return render(request, 'pages/home.html', context)


def books(request):
    category = request.GET.get('category')
    
    if category == None:
        book_cards = BookCardsModel.objects.all()
    else:
        book_cards = BookCardsModel.objects.filter(category__name=category)
        
    categories = BookCategoryModel.objects.all()

    context = {
        "book_cards": book_cards,
        "categories": categories
    }
    
    return render(request, 'pages/books.html', context)

# book details
def bookDetails(request, pk):
    book_detail = BookCardsModel.objects.get(id=pk)
    context = {
        'book_detail': book_detail
    }
    
    return render(request, 'details/book_details.html', context)

# shop details
def shopDetails(request, pk):
    shop_detail = BookCardsModel.objects.get(id=pk)
    context = {
        'shop_detail': shop_detail
    }
    return render(request, 'details/shop_details.html', context)

# card checkout to buy the book
def checkoutBookView(request, pk):
    checkout = BookCardsModel.objects.get(id=pk)

    context = {
        'checkout': checkout
    }
    
    return render(request, 'pages/checkout.html', context)
