from django.shortcuts import render
from django.http import HttpResponse

def function(request):
    return HttpResponse('Hey...Python..')

def function1(request):
    return render(request,'example.html')    

def function2(request):
    return render(request,'facebook login page.html')