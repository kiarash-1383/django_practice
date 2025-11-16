from django.test import TestCase
from .models import Book


class TestAPI(TestCase):
    def setUp(self):
        
        self.book1 = Book.objects.create(title="The Great Gatsby", genre="Classic")
        self.book2 = Book.objects.create(title="Dune", genre="Sci-Fi")
        self.book3 = Book.objects.create(title="The Hobbit", genre="Fantasy")
        self.book4 = Book.objects.create(title="Neuromancer", genre="Cyberpunk")
        self.book5 = Book.objects.create(title="1984", genre="Dystopian")
        self.book6 = Book.objects.create(title="Brave New World", genre="Dystopian")

    def test_genre_title_genre(self):

        expect = 'List of Books'
        
        expect_genre = 'genre'
        response = self.client.get(
            'book/Fantasy'
        )

        data = response.json()


        self.assertEqual(expect , data.get('title'))
        self.assertEqual(expect_genre , data.get('genre'))

    
    def test_genre(self) :

          excepted = list(Book.objects.filter(genre = 'Fantasy').values_list('id' , flat=True))
          
          response = self.client.get(
            'book/Fantasy'
        )

          data = response.json()

          result = data.get('books')

          self.assertEqual(excepted , result)