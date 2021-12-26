from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,username)
            redirect('')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was Created for '+form.cleaned_data.get('username'))
            return redirect("login")
    context = {'form':form}
    return render(request,'register.html',context)
    
def css(request):
    return render(request,'main.css')