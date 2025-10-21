from django.http import HttpResponse

from .models import Book
from .render import render_to_readable_output

def book_list(request):
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    author = request.GET.get('author', '')
    name = request.GET.get('name', '')


    try:
        min_price = int(min_price) if min_price is not None else 0
    except ValueError:
        min_price = 0

    try:
        max_price = int(max_price) if max_price is not None else 100000
    except ValueError:
        max_price = 100000

    books = Book.objects.filter(
        price__gte=min_price,
        price__lte=max_price,
        author__icontains=author,
        name__icontains=name
    )

    rendered_string = render_to_readable_output(books)
    return HttpResponse(rendered_string)
