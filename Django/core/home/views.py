from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def success(request):
    print("Hello")  
    return HttpResponse("success")
