
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from tasks.models import Task  # اگر مدل‌‌ت در همین مسیر است

@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        name = request.POST.get('task', '').strip()
        if not name:
            return HttpResponse("Task name is required!", content_type="text/plain", status=400)
        new_task = Task.objects.create(name=name)
        return HttpResponse(f"Task Created: '{new_task.name}'", content_type="text/plain")
    else:
        # اگر فقط POST مدنظرته، می‌تونی این بخش رو حذف کنی یا خطا بدی
        return HttpResponse("Method Not Allowed", content_type="text/plain", status=405)
