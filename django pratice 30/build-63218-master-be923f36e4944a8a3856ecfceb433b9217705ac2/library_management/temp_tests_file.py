from django.test import TestCase
from .models import *
from datetime import date, timedelta 




class AuthorBookModelTests(TestCase):

    def setUp(self):
    
        self.author1 = Author.objects.create(
            first_name="Ali",
            last_name="Hosseini",
            date_of_birth=date(1992, 9, 10),
            date_of_death=None  # زنده
        )
        self.author2 = Author.objects.create(
            first_name="Maryam",
            last_name="Rahimi",
            date_of_birth=date(1945, 1, 3),
            date_of_death=date(2017, 8, 25)  # درگذشته
        )
        self.author3 = Author.objects.create(
            first_name="Reza",
            last_name="Khodadadi",
            date_of_birth=date(1992, 9, 10),
            date_of_death=None
        )

        # ساخت چند کتاب برای هر نویسنده با تاریخ‌های انتشاری متفاوت
        self.book1 = Book.objects.create(
            title="Intro to Django",
            author=self.author1,
            summary="A practical guide to modern Django.",
            date_of_publish=date.today() - timedelta(days=365 * 2)  # ۲ سال پیش
        )
        self.book2 = Book.objects.create(
            title="Python Best Practices",
            author=self.author1,
            summary="Advanced tips and tricks for clean Python code.",
            date_of_publish=date.today() - timedelta(days=30)  # یک ماه پیش
        )
        self.book3 = Book.objects.create(
            title="Classic Literature",
            author=self.author2,
            summary="A poetic journey through 20th century literature.",
            date_of_publish=date.today() - timedelta(days=365 * 20)  # ۲۰ سال پیش
            
        )
    

    def test_author_is_live(self):
          

          result = self.author1.is_alive()



          result1 = self.author2.is_alive()

        


          self.assertTrue(result)

          self.assertFalse(result1)


    def test_author_get_age_aoutuor(self):
           
          result1 = self.author1.get_age()
          expected1 = 33
          self.assertEqual(expected1, result1.days // 365)

          result2 = self.author2.get_age()
          expected2 = 72
          self.assertEqual(expected2, result2.days // 365)


    
    def test_author_str(self):
         
             
             result = str(self.author1)

             exept = 'Ali Hosseini'

             self.assertEqual(exept , result)

    def test_book_get_age(self):

        result = self.book1.get_age()
        expected = 730
        self.assertEqual(expected, result.days)


    def test_book_str(self):


          result = str(self.book1)

          exept =  'Intro to Django'
           
          self.assertEqual(exept , result)


    def test_good_book(self):
          

        books = Book.objects.all()
        good_books = []
        bad_books = []

        for book in books:
           if book.get_age().days // 365 < 1:
             if book.author.get_age().days // 365 < 10:
                good_books.append(book)
             else:
                bad_books.append(book)
           else:
               bad_books.append(book)  # اینجا else رو می‌خوای برای شرط بالایی، نه کل حلقه

        response = self.client.get('/booklist/10/1/')  # اطمینان از اینکه مسیر درست با / تمام میشه

        html = response.content.decode()
        self.assertIn("<title>Booklist</title>", html)
        self.assertEqual(list(response.context['good_books']), good_books)
        self.assertEqual(list(response.context['bad_books']), bad_books)
