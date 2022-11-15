from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("joblist", views.joblist, name="joblist"),
    path("job/<int:pk>", views.job, name="job"),
    path("aplications/<int:pk>", views.aplications, name="aplications"),
    path("joblist/<str:cat>" , views.category, name='category'),
    path("joblisttwo/<str:cat>" , views.categorytwo, name='categorytwo')
    
    
    
    
]
