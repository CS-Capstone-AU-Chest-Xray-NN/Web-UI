from django.shortcuts import render, redirect
from django.http import HttpResponse

from webui.cnn import Model

model = Model()

def home(request):
    return render(request, 'main/index.html')
