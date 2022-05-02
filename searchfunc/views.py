from django.shortcuts import render
from .models import *
from django.db.models import Q

def home(request):
    
    if 's' in request.GET:
        search_key = request.GET['s']
        full_search = Q(Q(book_name__icontains=search_key) | Q(book_subtitle__icontains=search_key))
        book_cards = BookCardsModel.objects.filter(full_search)
    else:
        book_cards = BookCardsModel.objects.all()
        
        
    
    context = {
        "book_cards": book_cards,
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
