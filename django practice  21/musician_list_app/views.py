from django.views import View
from django.shortcuts import HttpResponse
from .models import Musician

class Musician_list(View):
    def get(self, request):
        names = list(Musician.objects.all().order_by('name').values_list('name', flat=True))
        return HttpResponse(names)
