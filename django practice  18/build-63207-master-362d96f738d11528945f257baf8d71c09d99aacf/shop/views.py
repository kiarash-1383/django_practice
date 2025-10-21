from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import Person
from django.http import HttpResponse

@csrf_exempt
def personal_page(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'main.html', context)

    elif request.method == 'POST':
        
        form_object = PersonalInformation(request.POST)    

        if form_object.is_valid() :
            
            full_name = form_object.cleaned_data.get('full_name')
            height = form_object.cleaned_data.get('height')
            gender = form_object.cleaned_data.get('gender')
            age = form_object.cleaned_data.get('age')

            ob_person = Person.objects.create(full_name = full_name , height = height , gender = gender , age = age)

            ob_person.save()

            return HttpResponse(ob_person , status = 201)
        
        else :

            return HttpResponse('Error' , status = 404)


