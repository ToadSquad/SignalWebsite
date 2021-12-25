from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def login(request):
    return render(request,'login.html')
    
def css(request):
    return render(request,'main.css')