from django.urls import path
from .views import profile, myprofile

urlpatterns = [
    # Add this
    path('edit_profile/', profile, name='users-profile'),
    path('myprofile/', myprofile, name='my-profile'),
]