from django.shortcuts import render, redirect
from django.http import HttpResponse
from MyApi.models import MyFile
from django.conf import settings

def Home(request):
    if request.method=="POST":
        img = request.FILES["image"]
        service = request.POST["service"]
        data = MyFile.objects.create(image = img)
        url = "http:127.0.0.1:8000" + data.image.url
        return redirect(url)
    return render(request, "index.html")