from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your views here.



#user list views

def index(request):  

    return render(request, 'users/index.html')
    
 
 
 
 #register views

def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        upform = UserProfileForm(request.POST)

        if form.is_valid() and upform.is_valid():
            user = form.save()

            profile = upform.save(commit=False)
            profile.user = user

            profile.save()

            # #after create profile this code block will logged in
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user)

        return redirect('signup')
        
    else:
        form = SignupForm()
        upform = UserProfileForm()

    context = {'signupform': form, 'upform':upform }

    return render(request, 'users/signup.html', context)
    
    




#login views

def login(request):
    return render(request, 'users/login.html')
