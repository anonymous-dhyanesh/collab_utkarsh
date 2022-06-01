from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def index(request):
    return render(request, "index.html")

def registerUser(request):
    if request.method == 'POST':

        username = request.POST['username'] 
        email = request.POST['email']
        password = request.POST['password']

        myuser = User.objects.create_user(username,email, password)
        myuser.save()
        
        return redirect("/")

    else:
        return render(request, "register.html")

def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # print(f"USERNAME : {username}")
        # print(f"PASSWORD : {password}")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("/")

        else:
            # login failed message here
            pass
    else:
        return render(request, 'login.html')

def logoutUser(request):
    return render(request, 'logout.html')

