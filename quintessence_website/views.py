import json

from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'index.html', context)


def project_manager(request):
    if request.method == 'POST':
        if request.POST.get('action_type') == "delete":
            Project.objects.filter(id=1).delete()
            print('deleted')
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'project_manager.html', context)


def request_handler(request):
    if request.method == 'POST':
        if request.POST.get('action_type') == "delete":
            Project.objects.filter(id=1).delete()
            print('deleted')
            response_data = {'deleted': 'true'}

            return HttpResponse(
                json.dumps(response_data),
                content_type="application/json"
            )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
