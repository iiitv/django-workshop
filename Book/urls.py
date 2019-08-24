from django.urls import path

from Book.views import view_single_book, view_all_books

urlpatterns = [
    path(r'<book_id>/', view_single_book, name='single-book'),
    path(r'', view_all_books, name='all-books')
]
