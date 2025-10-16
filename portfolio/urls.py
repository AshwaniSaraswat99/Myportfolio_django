from django.urls import path
from . import views

urlpatterns=[
    path("",views.home,name="home"),
    path('projects',views.projects,name="projects"),
    path('resume',views.resume,name="resume"),
    path('contact',views.contact_view,name="contact"),
    path('login',views.loginview,name="login"),
    path('register',views.register,name="register"),
    path('logout',views.logoutview,name="logout"),
]
