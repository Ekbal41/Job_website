from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .form import ProfileForm
from .models import Profile
from django.shortcuts import redirect



@login_required
def profile(request):
    profileform = ProfileForm()
    data = Profile.objects.get(user_id = request.user.id)
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            n = form.save(commit=False)
            n.user = request.user 
            n.save()
            return redirect('/profile/myprofile')
            
            
    else:
        profileform = ProfileForm()
        
    if data:
        pdata = data
    
    
    return render(request, 'tutoruser/profileedit.html',{'profileform': profileform, "data": pdata})


@login_required
def myprofile(request):
    
    data = Profile.objects.get(user_id = request.user.id)
    
    return render(request, 'tutoruser/myprofile.html',{'data': data})
    