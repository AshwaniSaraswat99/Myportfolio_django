from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,"home.html")
def projects(request):
    return render(request, "project.html")

def resume(request):
    return render(request, "resume.html")

def contact(request):
    return render(request, "contact.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")