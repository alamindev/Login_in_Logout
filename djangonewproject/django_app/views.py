from django.shortcuts import render,redirect
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import logout, login, authenticate
from django.conf import settings
# Create your views here.

def index(request):
    return render(request, "index.html")

def loginView(request):
    if request.user.is_authenticated:
        return redirect("django_app:index")
    else:
        if request.method =="POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect("django_app:index")
            else:              
                return render(request, "login.html")
                    
    return render(request, "login.html")
    
def get_logout(request):
    logout(request)
    return redirect("django_app:index")

def get_register(request):
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
    context = {
        'form':form
    }    
    return render(request, "form.html", context)    
