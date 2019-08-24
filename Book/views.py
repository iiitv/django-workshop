from django.shortcuts import render

from Book.models import Books

def view_all_books(request):
    objs = Books.objects.all()

    print(objs)
    context = {
        'books': objs
    }
    return render(request, 'view_all_books.html', context=context)


def view_single_book(request, *args, **kwargs):
    obj = Books.objects.get(id=kwargs['book_id'])

    context = {
        'book': obj
    }
    return render(request, 'view_single_book.html', context=context)
