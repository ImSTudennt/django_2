from django.shortcuts import render
from books.models import Book
from django.core.paginator import Paginator

books = Book.objects.all()

def books_view(request):
    template = 'books/books_list.html'
    context = {'books': books}
    return render(request, template, context)

def book_view(request, pub_date):
    paginator  = Paginator(books, 1)
    p_num = Book.objects.get(pub_date=pub_date).id
    page  = paginator.get_page(p_num)
    template = 'books/books_list.html'
    context = {'books': page,
               'page': page,}
    return render(request, template, context)


