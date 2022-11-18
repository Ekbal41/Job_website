from django.contrib import admin
from .models import Profile, Testimonial






class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'address', 'phone')

admin.site.register(Profile, ProfileAdmin)

class testimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'prof')

admin.site.register(Testimonial, testimonialAdmin)

