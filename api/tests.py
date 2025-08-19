# ...existing code...
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Author, Book

class APITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(first_name='Mark', last_name='Twain', birth_date='1835-11-30')
        self.book1 = Book.objects.create(title='Tom Sawyer', published_date='1876-01-01', author=self.author, genre='Fiction')
        self.book2 = Book.objects.create(title='Huckleberry Finn', published_date='1884-01-01', author=self.author, genre='Adventure')

    def test_create_author(self):
        response = self.client.post('/api/authors/', {'first_name': 'Jane', 'last_name': 'Austen', 'birth_date': '1775-12-16'})
        self.assertEqual(response.status_code, 201)

    def test_get_authors(self):
        response = self.client.get('/api/authors/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('books', response.data[0])

    def test_filter_books_by_genre(self):
        response = self.client.get('/api/books/?genre=Fiction')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
