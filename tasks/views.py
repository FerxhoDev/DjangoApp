from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm

# Create your views here.


def index(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Nota: Corregido el parámetro `username`.
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'User alredy exist'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'password do not mach'
        })


def tasks(request):
    return render(request, 'tasks.html')


def signout(request):
    logout(request)
    return redirect('home')


def signin(request):

    if request.method == 'GET':
        return render(request, 'signin.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password do not match'
            })
        else:
            login(request, user)
            return redirect('tasks')

def createtask(request):

    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
                'form': TaskForm,
                'error': 'Bad data passed in. Try again'
            })

    