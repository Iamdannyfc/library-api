# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Category, Book
from .serializers import CategorySerializer, BookSerializer

class LibraryApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Create sample category
        self.category = Category.objects.create(name='Test Category')

        # Create sample book
        self.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            no_of_pages=100,
            description='Test Description',
            category=self.category
        )

    def test_get_categories(self):
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_category(self):
        data = {'name': 'New Category'}
        response = self.client.post('/categories/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_get_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'author': 'New Author',
            'no_of_pages': 200,
            'description': 'New Description',
            'category': self.category.id
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        data = {
            'title': 'Updated Title',
            'author': 'Updated Author',
            'no_of_pages': 150,
            'description': 'Updated Description',
            'category': self.category.id
        }
        response = self.client.put(f'/books/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        response = self.client.delete(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
