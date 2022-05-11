from multiprocessing import context
from django.shortcuts import render, reverse
from .models import *
from django.views.generic import *
from .forms import *
from django.db.models import Q

# base home
def home(request):
    sliders = SliderImagesContent.objects.all()
    whocontents = WhoWeAreModel.objects.all()
    essentials = EssentialsPageModel.objects.all()
    essential_right_content = EssentialRightContent.objects.all()
    count_values = CountPageModel.objects.all()
    books_to_read = BooksToRead.objects.all()
    contact_me_context = ContactMePartContext.objects.all()
    context = {
        'sliders': sliders,
        'whocontents': whocontents,
        'essentials': essentials,
        'essential_right_content': essential_right_content,
        'count_values': count_values,
        'books_to_read': books_to_read,
        'contact_me_context': contact_me_context,
    }
    return render(request, 'pages/home.html', context)

# book page
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

# create sign up view
class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm
    
    def get_success_url(self):
        return reverse('login')
