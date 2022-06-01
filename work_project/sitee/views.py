from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def registerUser(request):
    return render(request, "register.html")

def loginUser(request):
    return render(request, 'loign.html')

def logoutUser(request):
    return render(request, 'logout.html')

