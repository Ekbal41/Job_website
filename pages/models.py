from django.db import models
from ckeditor.fields import RichTextField

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
    cv = RichTextField()
    
    
    
    def __str__(self):
        return self.name