from django.http import HttpResponse
from django.shortcuts import render
from .models import Usuario

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "home.html", {"usuarios": usuarios})

