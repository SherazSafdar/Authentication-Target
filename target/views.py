from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login
from user_registration.models import UserProfile


def register_user(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        User.objects.create_user(username=username, email=email, password=password)
        return render(request, 'registration_success.html')
    return render(request, 'register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'registration_success.html')
        else:
            return render(request, 'login.html')
    return render(request, 'login.html')


 # profile view function
def view_profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        return render(request, 'profile.html', {'profile': user_profile})
    else:
        return redirect('login')
    

 # profile update function
def update_profile(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)

        if request.method == 'POST':
            # Update user profile fields
            user_profile.date_of_birth = request.POST['date_of_birth']
            user_profile.phone_number = request.POST['phone_number']
            user_profile.address = request.POST['address']
            user_profile.save()
            return redirect('view_profile')

        return render(request, 'profile_update.html', {'profile': user_profile})
    else:
        return redirect('login')
 
        
