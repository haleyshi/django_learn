#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    #return HttpResponse("Hello Django!")
    context = {}
    context['hello'] = "Hello Django!"
    context['welcome'] = "Welcome to th Django World!"
    return render(request, 'hello.html', context)