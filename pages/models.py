from django.db import models
import django_filters
from ckeditor.fields import RichTextField
from accounts.models import CustomUser

# Create your models here.

class Job(models.Model): 
    
    CHOICES =(
    ("English V", "English V"),
    ("Bangla V", "Bangla V"),
    ("Arabic V", "Arabic V"),
     
    )
    
    GEN =(
    ("Male", "Male"),
    ("Female", "Female"),
     ("Other", "Other"),
    )
    CAT =(
    ("School", "School"),
    ("College", "College"),
     ("University", "University"),
    )
    SEC =(
    ("Science", "Science"),
    ("Arts", "Arts"),
    ("Business", "Business"),
     ("Other", "Other"),
    )
    STA =(
    ("Available", "Available"),
    ("NotAvailable", "NotAvailable"),
    ("Pending", "Pending"),
     ("Other", "Other"),
    )
    aplicants = models.ManyToManyField(CustomUser,blank=True)
    title=models.CharField(max_length=50)
    category=models.CharField(max_length=50,choices = CAT)
    sclass=models.CharField(max_length=50)
    Vtype=models.CharField(max_length=50,choices = CHOICES)
    gender=models.CharField(max_length=50,choices = GEN)
    overview = RichTextField()
    
    
    location=models.CharField(max_length=150)
    section =models.CharField(max_length=50,choices = SEC)
    uni=models.CharField(max_length=50)
    teacherdpt=models.CharField(max_length=50)
    teacherback=models.CharField(max_length=50,choices = CHOICES)
    teachergender=models.CharField(max_length=50,choices = GEN)
    salary=models.PositiveIntegerField(default=3000)
    date=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,default="Available",choices = STA)
      

    def __str__(self):
        return self.title


class Teacher(models.Model):
    name=models.CharField(max_length=50,null=True)
    university=models.CharField(max_length=50,null=True)
    phone=models.CharField(max_length=50,null=True)
    cv = RichTextField()
    
    
    
    def __str__(self):
     if self.name==None:
         return "TEACHER NAME IS NULL"
     return self.name
    
    
class Aplications(models.Model):
        
    name=models.CharField(max_length=50)
    university=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    appliedtuition = models.CharField(max_length=100, null= True)
    tuitionid = models.CharField(max_length=10, null=True)
    cv = RichTextField()
    
    
    def tuition_page(self):
       
        from django.utils.html import format_html
        return format_html("<a href='/job/%s'>%s</a>" % (self.tuitionid, self.appliedtuition))
    
    
    def __str__(self):
        return self.name
    

    
class JobFilter(django_filters.FilterSet):
    STATUS_CHOICES = (
    ('Available', 'Available'),
    ('NotAvailable', 'NotAvailable'),
    ('Pending', 'Pending'),
)
    
    GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    
)
    
    V_CHOICES = (
    ('English V', 'English Version'),
    ('Bangla V', 'Bangla Version'),
    ('Arabic V', 'Arabic Version'),
    
)
    title = django_filters.CharFilter(lookup_expr='icontains',label='Word in Title')
    status = django_filters.ChoiceFilter(lookup_expr='iexact',choices=STATUS_CHOICES, label='Tuition status')
    gender = django_filters.ChoiceFilter(lookup_expr='iexact',choices=GENDER_CHOICES, label='Student Gender')
    Vtype = django_filters.ChoiceFilter(lookup_expr='iexact',choices=V_CHOICES, label='Version')
    sclass = django_filters.CharFilter(lookup_expr='icontains', label='Class')
   

class Meta:
    model = Job
    fields = ['title','status','gender','Vtype' 'sclass' 'date']