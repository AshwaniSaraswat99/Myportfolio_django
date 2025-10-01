from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path('projects',views.projects,name="projects"),
    path('resume',views.resume,name="resume"),
    path('contact',views.contact,name="contact"),
    path('login',views.login,name="login"),
    path('register',views.register,name="register"),
]
