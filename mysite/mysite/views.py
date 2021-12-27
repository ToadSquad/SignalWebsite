from django.shortcuts import redirect, render
from django.http import HttpResponse

from django.contrib.auth.forms import UserCreationForm

from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages


# Create your views here.
#@login_required(login_url='/login')
def homepage(request):
    return render(request,'homepage.html')

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is Incorrect')

    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('/login')
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was Created for '+form.cleaned_data.get('username'))
            return redirect("/login")
    context = {'form':form}
    return render(request,'register.html',context)
    
def css(request):
    return render(request,'main.css')