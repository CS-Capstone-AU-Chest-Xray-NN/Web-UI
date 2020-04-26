from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from webui.cnn import Model
from webui.cnn.models import Image

model = Model()

def home(request):
    if request.method == 'POST':
        image = Image.create(request.FILES['upload'])
        image.save()
        diagnoses = model.predict(image.image.path)
        return render(request, 'main/index.html', {
            'url': image.image.url,
            'diagnoses': diagnoses,
        })
    return render(request, 'main/index.html')
