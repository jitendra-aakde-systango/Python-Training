from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples=[
        {'name':'Jitendra', "age":23}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        ]
    return render(request, "index.html", context={'peoples':peoples})

def about(request):
    peoples=[
        {'name':'Jitendra', "age":23}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        ]
    return render(request, "about.html", context={'peoples':peoples})

def contact(request):
    peoples=[
        {'name':'Jitendra', "age":23}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        {'name':'vivekk', "age":24}, 
        ]
    return render(request, "contact.html", context={'peoples':peoples})