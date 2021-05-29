from django.shortcuts import render ,redirect
from .forms import *
from .models import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required


# Create your views here
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            admin=form.save()
            login(request,admin)

            return redirect("home")
    else:
        form = RegisterForm()

    return render(request, "register/register.html", {"form": form})



def loginuser(request):
    if request.method=='GET':
        return render(request,'registration/login.html', {'form':AuthenticationForm()})
    else:
        user= authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'registration/login.html', {'form':AuthenticationForm(),'error':'Enter Correct Info'})
        else:
            login(request,user)
            return redirect('home')


@login_required
def logoutuser(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')
