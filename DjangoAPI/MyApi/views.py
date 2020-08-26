from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    if request.method=="POST":
        print(request.FILES, request.POST)
    return render(request, "index.html")