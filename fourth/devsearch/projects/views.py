from django.shortcuts import render
from .models import Project

# Create your views here.
def projects(request):
    pr = Project.objects.all()

    context = {
        'projects': pr
    }

    return render(request, 'projects/projects.html', context)