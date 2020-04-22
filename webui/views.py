from django.shortcuts import render, redirect
from django.http import HttpResponse

#home is the login page
def home(request):
    return render(request, 'main/index.html')
