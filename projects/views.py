from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .form import ProjectForm

@login_required
def project_list(request):
    user = request.user
    if user.profile.is_admin():
        projects = Project.objects.all()
    else:
        projects = user.projects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

@login_required
def project_create(request):
    if not request.user.profile.is_admin():
        return redirect('dashboard')
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            form.save_m2m()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/project_form.html', {'form': form})