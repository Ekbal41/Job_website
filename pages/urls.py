from django.urls import path
from django.conf import settings

from . import views
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="home"),
    path("joblist", views.joblist, name="joblist"),
    path("job/<int:pk>", views.job, name="job"),
    path("aplications/<int:pk>", views.aplications, name="aplications"),
    path("joblist/<str:cat>" , views.category, name='category'),
    path("joblisttwo/<str:cat>" , views.categorytwo, name='categorytwo'),
    path('list/', views.job_list, name="job-list")
    
    
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
