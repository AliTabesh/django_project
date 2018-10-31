from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1 style='font-style: italic; text-align: center; margin: 50vh;'>Hello<span> world!</span></h1>")
