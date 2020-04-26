from django.shortcuts import render, redirect
from django.http import HttpResponse

from webui.cnn import Model
from webui.cnn.models import Image

model = Model()

def home(request):
    return render(request, 'main/index.html')

def upload(request):
    if request.method == 'POST':
        file = request.FILES['upload']
        image = Image.create(file)
        image.save()
        return redirect('/')
