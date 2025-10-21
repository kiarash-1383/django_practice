from django.http import HttpResponse

from django.http import HttpResponse



def sad (request , name):


     return HttpResponse(f'Nobody likes you, {name}!')


def  good  (request , name , times):
     
    msg = ("You are great, {} :)<br>".format(name)) * times
    return HttpResponse(msg)