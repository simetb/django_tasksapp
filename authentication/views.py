from django.shortcuts import render, HttpResponse, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# Views
def login_view(request):
    return render(request, 'login.html',{})

def signin_view(request):
    return render(request, 'signin.html',{})

# Functions 
# Signin
def dosignin_ep(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

# Login
def dologin_ep(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) 
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            print("Error al hacer login")
            return render(request,'login.html')
        
    else:
        return render(request, 'login.html')
    
# logout
def dologout_ep(request):
    logout(request)
    return redirect('login')

        
        
            