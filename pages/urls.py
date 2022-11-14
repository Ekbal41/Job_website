from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("joblist", views.joblist, name="joblist"),
    path("job/<int:pk>", views.job, name="job"),
    
    
    
    
]
