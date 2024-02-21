from django.shortcuts import render, HttpResponse
from .forms import SignUpForm

# Create your views here.

# Views
def login_view(request):
    return render(request, 'login.html',{})

def signin_view(request):
    return render(request, 'signin.html',{})

# Functions
def dosignin_ep(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registro Exitoso")
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})