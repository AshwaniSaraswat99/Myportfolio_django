import requests
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import contact as ContactMessage
from .forms import contactform, registrationform
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

# Create your views here.
def home(request):
    return render(request,"home.html")
def projects(request):
    return render(request, "project.html")

def resume(request):
    return render(request, "resume.html")

def loginview(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
                messages.error(request, "Invalid username or password.")
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        form=registrationform(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account has been created successfully!!')
            return redirect('login')
        else:
            messages.error(request, 'Please check the details you have entered or try to log in if you already have an account.')
            return render(request, "register.html", {'form': form})
    else:
        form=registrationform(request.POST)
        return render(request, "register.html", {'form': form})

def logoutview(request):
    auth_logout(request)
    messages.success(request, "You have been logged out successfully.")
    return redirect('login')

def contact(request):
    if request.method=='POST':
        form=contactform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully!')
    else:
        form=contactform()
    return render(request, "contact.html", {'form': form})

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        # Save to database
        contact = ContactMessage.objects.create(name=name, email=email, message=msg)

        # Send email
        send_mail(
            subject=f"New Contact Message from {name}",
            message=f"Name: {name}\nEmail: {email}\nMessage:\n{msg}",
            from_email=None,       # uses DEFAULT_FROM_EMAIL
            recipient_list=['your_email@gmail.com'],  # where you want to receive
        )

        messages.success(request, "Your message has been sent successfully!")
    
    return render(request, "contact.html")


'''def projects(request):
    response = requests.get("http://127.0.0.1:8000/api/projects/")
    projects = response.json()
    return render(request, "project.html", {'projects': projects})'''