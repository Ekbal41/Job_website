from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from .models import Job, Teacher, Aplications



def index(request):
    jobs = Job.objects.order_by('-date')[:6]
    
    return render(request,'tutor/index.html',{'jobs': jobs})

def category(request, cat):
    
    if cat == 'all':
       jobs =Job.objects.order_by('-date')
    elif cat == 'bangla':        
       jobs =Job.objects.filter(Vtype = 'Bangla V').order_by('-date')
    elif cat == 'english':
       jobs =Job.objects.filter(Vtype = 'English V').order_by('-date')
    elif cat == 'male':
       jobs =Job.objects.filter(gender = 'Male').order_by('-date')
    elif cat == 'female':
       jobs =Job.objects.filter(gender = 'Female').order_by('-date')
    elif cat == 'available':
       jobs =Job.objects.filter(status = 'Available').order_by('-date')
    else:
        pass
   
        
        
    
    
    return render(request,'tutor/index.html',{'jobs': jobs})

def categorytwo(request, cat):
    
    if cat == 'all':
       jobs =Job.objects.order_by('-date')
    elif cat == 'bangla':        
       jobs =Job.objects.filter(Vtype = 'Bangla V').order_by('-date')
    elif cat == 'english':
       jobs =Job.objects.filter(Vtype = 'English V').order_by('-date')
    elif cat == 'male':
       jobs =Job.objects.filter(gender = 'Male').order_by('-date')
    elif cat == 'female':
       jobs =Job.objects.filter(gender = 'Female').order_by('-date')
    elif cat == 'available':
       jobs =Job.objects.filter(status = 'Available').order_by('-date')
    else:
        pass
    
    page_num = request.GET.get('page', 1)

    paginator = Paginator(jobs, 6) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

   
        
        
    
    
    return render(request,'tutor/joblist.html',{'jobs': jobs, 'page_obj': page_obj })


def joblist(request):
    jobs = Job.objects.order_by('-date')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(jobs, 6) # 6 employees per page


    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    
    return render(request,'tutor/joblist.html',{'jobs': jobs,'page_obj': page_obj })

def job(request, pk):
    job = Job.objects.get(id =pk)
    
    return render(request,'tutor/job.html',{'job': job},)

def aplications(request, pk):
    if request.method=='POST':
        
       
        
        job = Job.objects.get(id =pk)
        if job.status == "NotAvailable":
            pass
        else:
            job.status ='Pending'
            job.save()
        
        
        tphone = request.POST.get('phone')
        oldteacher = Teacher.objects.filter(phone=tphone).exists()
        
        if oldteacher:
            pass
        else:
            
            tfirstname = request.POST.get('firstname')
            tlastname = request.POST.get('lastname')
            name = str(tfirstname)+str(tlastname)
        
            tcov = request.POST.get('cover')
            tuniversity= request.POST.get('uni')
            tphone = request.POST.get('phone')
            teacher=Teacher(name=name,cv=tcov,university=tuniversity,phone=tphone)
            teacher.save()
        
        if job.status == "NotAvailable":
            pass
        else:
            job.status ='Pending'
            job.save()
            tfirstname = request.POST.get('firstname')
            tlastname = request.POST.get('lastname')
            name = str(tfirstname)+str(tlastname)
        
            tcov = request.POST.get('cover')
            tuniversity= request.POST.get('uni')
            tphone = request.POST.get('phone')
            aplication=Aplications(name=name,cv=tcov,university=tuniversity,phone=tphone)
            aplication.save()      
    
    
        return redirect("/")
    
    


