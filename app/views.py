from django.shortcuts import render, redirect
from . forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        return redirect("/register")

def signup(request):
    if request.method == "POST":
       form = NewUserForm(request.POST)
       if form.is_valid():
           user = form.save()
           return HttpResponse("Registration successfull. Now You can login into your acount")
    form = NewUserForm
    return render(request, "register.html", {"newuser":form})

def signin(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    else:
        if request.method == "POST":
            user_details = AuthenticationForm(request, request.POST)
            if user_details.is_valid():
                username = user_details.cleaned_data.get("username")
                password = user_details.cleaned_data.get("password")
                cred = authenticate(username= username, password = password)
                if cred is not None:
                    login(request, cred)
                    messages.info(request, "You are logged in")
                    return redirect("/index")
            else:
                messages.error(request, "wrong credentials")
        else:
            messages.error(request, "wrong credentials")
    user_details = AuthenticationForm()
    return render(request, "signin.html", {"user":user_details})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("/register")