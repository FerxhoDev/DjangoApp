from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Nota: Corregido el parámetro `username`.
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('User created successfully')
            except Exception as e:
                # Puedes usar `str(e)` para diagnosticar el error exacto si es necesario.
                return HttpResponse('User already exists ' + str(e))
        return HttpResponse('Passwords do not match')
