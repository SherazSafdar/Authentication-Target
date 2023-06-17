from django.shortcuts import render, redirect
from django.contrib.auth.models import User 
from .forms import UserRegistrationForm

#register function
def register(request):
    if request.method=='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'registration_success')
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form': form})    
        
        
            


#def register_user(request):
#    if request.method=='POST':
#        username = request.POST['username']
#        email = request.POST['email']
#        password = request.POST['password']
#        User.objects.create_user(username=username, email=email, password=password)
#        return render(request, 'registration_success.html')
#    return render(request, 'register.html')

