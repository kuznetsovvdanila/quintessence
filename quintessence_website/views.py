from django.shortcuts import render
from .models import *


def index(request):

    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'index.html', context)
