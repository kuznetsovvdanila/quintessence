import json

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'index.html', context)


def project_manager(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'project_manager.html', context)


def project_editor(request, pk):
    context = {
        'project': Project.objects.filter(id=pk)[0]
    }
    return render(request, 'editor.html', context)


def new_project_editor(request):
    context = {}
    return render(request, 'editor.html', context)


def request_handler(request):
    response_data = {}

    def delete_project():
        Project.objects.filter(id=request.POST.get('id')).delete()
        return {'action_type': 'delete',
                'status': 'succeeded'}

    def create_project():
        new_project = Project()
        new_project.name = request.POST.get('name')
        new_project.description = request.POST.get('description')
        new_project.save()
        return {'action_type': 'create_project',
                'status': 'succeeded',
                'id': new_project.id,
                'name': new_project.name,
                'description': new_project.description}

    def update_project():
        project = Project.objects.filter(id=request.POST.get('id'))[0]
        project.name = request.POST.get('name')
        project.description = request.POST.get('description')
        project.save()
        return {'action_type': 'update_project',
                'status': 'succeeded',
                'name': project.name,
                'description': project.description}

    def auth():
        user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return {'action_type': 'auth',
                    'status': 'succeeded'}
        else:
            return {'action_type': 'auth',
                    'status': 'failed'}

    def loging_out():
        logout(request)
        return {'action_type': 'logout',
                'status': 'succeeded'}

    if request.method == 'POST':
        if request.POST.get('action_type') == 'create_project':
            response_data = create_project()
        if request.POST.get('action_type') == "delete":
            response_data = delete_project()
        if request.POST.get('action_type') == 'update_project':
            response_data = update_project()
        if request.POST.get('action_type') == 'auth':
            response_data = auth()
        if request.POST.get('action_type') == 'logout':
            response_data = loging_out()

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
