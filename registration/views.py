from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                messages.error(request, "Unsuccessful registration. Invalid information.")
                return render (request,'appuser/signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                auth.login(request,user)
                messages.success(request, "Registration successful." )
                return redirect('homepage')
        else:
            return render (request,'registration/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'registration/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            messages.info(request, f"You are now logged in as {user['username']}.")
            return redirect('homepage')
        else:
            messages.error(request,"Invalid username or password.")
            return render (request,'registration/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'registration/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, "You have successfully logged out.") 
    return redirect('homepage')
# ====================================================
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def indexView(request):
    return render(request,'index.html')
@login_required()

def dashboardView(request):
    return render(request,'registration/dashboard.html')

def registerView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request,'registration/signup.html',{'form':form}) 
