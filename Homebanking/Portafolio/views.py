from django.shortcuts import render
from .models import Proyectos
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def portafolio(request):
    projects = Proyectos.objects.all() 
    return render(request, 'portafolio.html', {'projects': projects })