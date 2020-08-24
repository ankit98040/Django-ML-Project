from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    return HttpResponse("<center>Hello All Present Here. Welcome to Home Page</center>")

