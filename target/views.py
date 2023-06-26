from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import UserProfileForm

#register function
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})  

#registration_success function
def registration_success(request):
    return render(request, 'registration_success.html')

#login function
def login_view(request):
    if request.method=="POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                #redirect succes page
                return redirect('registration_success')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})        
    
# users to view their profiles function

def profile(request):
    if request.method=="POST":
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            if request.user.is_authenticated:
                profile.user = request.user
                profile.save()
                return redirect('profile_create')
        else:
            return render(request,'profile_create.html',{'form':form})
    else:
        form = UserProfileForm()
        return render(request, 'login.html', {'form':form})
    
#profile create successfull function
def profile_create(request):
    return render(request, 'profile_create.html')
                 

# users to update their profiles function        
        
def update_profile(request):
    user_profile = request.user.userprofile
    
    if request.method=="POST":
        form = UserProfileForm(request.POST, instance=user_profile)    
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
        
    return render(request, 'update_profile.html', {'form':form})         


#def register_user(request):
#    if request.method=='POST':
#        username = request.POST['username']
#        email = request.POST['email']
#        password = request.POST['password']
#        User.objects.create_user(username=username, email=email, password=password)
#        return render(request, 'registration_success.html')
#    return render(request, 'register.html')

