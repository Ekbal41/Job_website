from django.shortcuts import render
from .models import Job


def index(request):
    jobs = Job.objects.order_by('-date')[:6]
    
    return render(request,'tutor/index.html',{'jobs': jobs})

def joblist(request):
    
    return render(request,'tutor/joblist.html')

def job(request, pk):
    job = Job.objects.get(id =pk)
    
    return render(request,'tutor/job.html',{'job': job})

