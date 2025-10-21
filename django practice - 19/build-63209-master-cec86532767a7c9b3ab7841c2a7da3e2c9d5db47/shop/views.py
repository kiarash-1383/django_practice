from django.http import HttpResponse
from django.shortcuts import render

from .forms import PersonalInformation
from .models import Person


def show_people(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        context = {
            'persons': persons
        }
        return render(request, 'show_people.html', context)


def submit_person(request):
    if request.method == 'GET':
        
       form_object = PersonalInformation()

       return render (request , 'new_person.html' , context= { 'form_object' : form_object}) 
        

    elif request.method == 'POST':
        
        form_object = PersonalInformation(request.POST)

        if form_object.is_valid() :
            
            full_name = form_object.cleaned_data.get('full_name')
            height = form_object.cleaned_data.get('height')
            gender = form_object.cleaned_data.get('gender')
            age = form_object.cleaned_data.get('age')

            new_person = Person.objects.create( full_name = full_name , height = height , gender = gender , age = age)
            
            new_person.save()

            return HttpResponse(new_person , status = 201)
        
        else :

            return HttpResponse('Error' , status = 404)
