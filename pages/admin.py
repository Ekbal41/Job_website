from django.contrib import admin
from .models import Job, Teacher, Aplications

# Register your models here.

class JobAdmin(admin.ModelAdmin):
    list_display = ( 'title', 'sclass', 'status')
    
admin.site.register(Job, JobAdmin)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone', 'university')
    
admin.site.register(Teacher, TeacherAdmin)


class AplicationsAdmin(admin.ModelAdmin):
    list_display = ( 'name', 'phone', 'university', 'tuition_page')
    
admin.site.register(Aplications, AplicationsAdmin)
