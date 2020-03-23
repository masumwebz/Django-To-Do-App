from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    
    


# update profile views
#

#login views
# login page views
def loginpage(request):
    # if request.user.is_authenticated:
    #     return redirect('user_list')
    # else:

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'pass ki vule gesen?')
        context = {}

        return render(request,'users/login.html',context)




def logoutuser(request):
    logout(request)
    return redirect('login')