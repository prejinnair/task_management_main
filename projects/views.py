from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Project
from .forms import ProjectForm
from .decorators import is_admin

@user_passes_test(is_admin)
def project_list(request):
    projects = Project.objects.select_related('team').all()
    return render(request, 'projects/project_list.html', {'projects': projects})

@user_passes_test(is_admin)
def project_create(request):
    form = ProjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('projects:project_list')
    return render(request, 'projects/project_form.html', {'form': form})

@user_passes_test(is_admin)
def project_update(request, pk):
    project = get_object_or_404(Project, pk=pk)
    form = ProjectForm(request.POST or None, instance=project)
    if form.is_valid():
        form.save()
        return redirect('projects:project_list')
    return render(request, 'projects/project_form.html', {'form': form, 'project': project})

@user_passes_test(is_admin)
def project_delete(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects:project_list')
    return render(request, 'projects/project_confirm_delete.html', {'project': project})


def project_detail(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    return render(request, 'projects/project_detail.html', {'project': project})
