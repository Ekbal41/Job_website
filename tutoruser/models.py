from django.db import models
from accounts.models import CustomUser
from django.dispatch import receiver 
from django.db.models.signals import post_save 

# Create your models here.
# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, primary_key=True, on_delete=models.CASCADE)

    avatar = models.ImageField(default='male.png', upload_to='profile_images')
    firstname = models.CharField(null=True,max_length=20)
    lastname = models.CharField(null=True,max_length=20)
    educationlevel = models.CharField(null=True,max_length=40)
    age = models.IntegerField(null=True)
    bio = models.TextField(null=True)
    address = models.CharField(null=True,max_length=50)
    phone = models.CharField(null=True,max_length=50)
    email = models.CharField(null=True,max_length=70)
    religion= models.CharField(null=True,max_length=70)
    ongoingtuition =models.CharField(null=True,max_length=70)
    experience =models.TextField(null=True,max_length=70)
    university = models.CharField(null=True,max_length=40)
    depertment = models.CharField(null=True,max_length=40)
    
    facebook =models.CharField(null=True,max_length=70)
    twitter =models.CharField(null=True,max_length=70)
    linkedin =models.CharField(null=True,max_length=70)
    youtube =models.CharField(null=True,max_length=70)
    
    @receiver(post_save, sender=CustomUser) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save, sender=CustomUser)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
            

	

    def __str__(self):
        return self.user.username
