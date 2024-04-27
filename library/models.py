
from django.db import models

class Category(models.Model):
    # Model representing a category of books
    name = models.CharField(max_length=100)  # Name of the category
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the category was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the category was last updated

    def __str__(self):
        return self.name

class Book(models.Model):
    # Model representing a book
    title = models.CharField(max_length=200)  # Title of the book
    author = models.CharField(max_length=100)  # Author of the book
    no_of_pages = models.IntegerField()  # Number of pages in the book
    description = models.TextField()  # Description of the book
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='books')  # Category of the book
    created_at = models.DateTimeField(auto_now_add=True)  # Date and time when the book was created
    updated_at = models.DateTimeField(auto_now=True)  # Date and time when the book was last updated

    def __str__(self):
        return self.title