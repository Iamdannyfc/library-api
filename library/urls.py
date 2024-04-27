
from django.urls import path
from .views import category_list_create, category_detail, book_list_create, book_detail

urlpatterns = [
    path('categories/', category_list_create, name='category-list-create'),  # Endpoint for listing and creating categories
    path('categories/<int:pk>/', category_detail, name='category-retrieve-update-delete'),  # Endpoint for retrieving, updating, and deleting categories
    path('books/', book_list_create, name='book-list-create'),  # Endpoint for listing and creating books
    path('books/<int:pk>/', book_detail, name='book-retrieve-update-delete'),  # Endpoint for retrieving, updating, and deleting books
]
