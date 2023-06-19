from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate, login
from .forms import LoginForm

#register function
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success.html')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})  


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
                return redirect('registration_succes.html')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form':form})        
        
        
            


#def register_user(request):
#    if request.method=='POST':
#        username = request.POST['username']
#        email = request.POST['email']
#        password = request.POST['password']
#        User.objects.create_user(username=username, email=email, password=password)
#        return render(request, 'registration_success.html')
#    return render(request, 'register.html')

