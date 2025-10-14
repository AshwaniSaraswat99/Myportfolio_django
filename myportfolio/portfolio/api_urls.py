from django.urls import path
from .api_views import ProjectDetailView, ProjectView

urlpatterns = [
    path('projects/', ProjectView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),  # Detail view for a specific project
]