from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Task

@csrf_exempt
def delete_task(request, task_id):
    if request.method == 'DELETE':
        try:
            task = Task.objects.get(id=task_id)
            task_name = task.name
            task.delete()
            return HttpResponse(f"Task Done: '{task_name}'", content_type="text/plain")
        except Task.DoesNotExist:
            return HttpResponse(
                f"There isn't any task with id '{task_id}'",
                content_type="text/plain",
                status=404
            )
    else:
        return HttpResponse(
            "Method Not Allowed",
            content_type="text/plain",
            status=405
        )
