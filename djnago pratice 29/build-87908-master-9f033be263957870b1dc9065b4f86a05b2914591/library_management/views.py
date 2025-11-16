from django.http import JsonResponse
from .models import *

def books(request, genre) -> JsonResponse:
    
    return JsonResponse(data={
        'title': 'List of Books',
        'genre': genre,
        'books': list(Book.objects.filter(genre=genre).values_list('id', flat=True))
    })
