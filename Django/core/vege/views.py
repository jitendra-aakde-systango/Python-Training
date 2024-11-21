from django.shortcuts import render, redirect
from .models import *
# Create your views here.
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image') 
        Receipe.objects.create(
            receipe_name=receipe_name, 
            receipe_description=receipe_description,
            receipe_image=receipe_image
        )
        return redirect('/receipes')

    queryset=Receipe.objects.all()
    context={'receipes':queryset}   
        
    return render(request, "receipes.html",context)

@login_required(login_url="/login")
def delete_receipe(request, id):
    print('recipe deleted')
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes')

@login_required(login_url="/login")
def update_receipe(request, id):
    print('Update receipe')
    queryset=Receipe.objects.get(id=id)

    if request.method=="POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image') 

        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        if receipe_image:
            queryset.receipe_image=receipe_image

        queryset.save()
        return redirect('/receipes')



    context={'receipe':queryset}
    return render(request,'update_receipes.html', context )

def login_page(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user_exist = User.objects.filter(email=email).first()
        if not user_exist:
            messages.error(request, "User does not exist. Please register.")
            return redirect('/register')

        username = user_exist.username  
        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, "Incorrect password.")
            return redirect('/login')

        login(request, user)
        return redirect('/receipes')

    return render(request, "login.html")

def register(request):
    
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get("email")
        password = request.POST.get("password")

        userExist = User.objects.filter(email=email).exists()
        if userExist:
            messages.error(request, "Already Registered. Please login.")
            return redirect('/register/')

        username = email.split('@')[0]

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. Please choose another.")
            return redirect('/register/')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        user.set_password(password)
        user.save()

        messages.success(request, "User created successfully.")
        return redirect('/login/')

    return render(request, "register.html")

@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return redirect('/login')