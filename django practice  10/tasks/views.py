from .models import *
from django.http import HttpResponse

def list_create_tasks(request):
    if request.method == 'GET':
        query = Task.objects.all().order_by('name')
      
        result = '\n'.join(task.name for task in query)
        return HttpResponse(result, content_type="text/plain")

def count_tasks(request):
    if request.method == 'GET':
        count = Task.objects.all().count()
        return HttpResponse(f'You have \'{count}\' tasks to do')
