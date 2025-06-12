from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from accounts.models import User, UserProfile
from teams.models import Team
from projects.models import Project
from accounts.utils import send_verification_email
from accounts.forms import UserCreationForm, UserChangeForm
import string
import random

def is_admin(user):
    return user.is_authenticated and user.is_superuser

@login_required
@user_passes_test(is_admin)
def dashboard(request):
    current_user = request.user
    user_profile = get_object_or_404(UserProfile, user=current_user)

    user_count = User.objects.count()
    team_count = Team.objects.count()
    project_count = Project.objects.count()
    context = {
        'user_profile': user_profile,
        'user_count': user_count,
        'team_count': team_count,
        'project_count': project_count
    }
    print(context, "context")
    return render(request, 'adminpanel/dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def user_list(request):
    users = User.objects.all()
    return render(request, 'adminpanel/user_list.html', {'users': users})

@login_required
@user_passes_test(is_admin)
def user_create(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            teams = request.POST.getlist('teams')
            projects = request.POST.getlist('projects')
            user.teams.set(teams)
            user.projects.set(projects)
            messages.success(request, "User created successfully.")
            return redirect('admin_panel:user_list')
    else:
        form = UserCreationForm()
    
    teams = Team.objects.all()
    projects = Project.objects.all()
    return render(request, 'adminpanel/user_create.html', {
        'form': form,
        'teams': teams,
        'projects': projects
    })

@login_required
@user_passes_test(is_admin)
def user_edit(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            teams = request.POST.getlist('teams')
            projects = request.POST.getlist('projects')
            user.teams.set(teams)
            user.projects.set(projects)
            messages.success(request, "User updated successfully.")
            return redirect('admin_panel:user_list')
    else:
        form = UserChangeForm(request.POST, instance=user)

    teams = Team.objects.all()
    projects = Project.objects.all()
    return render(request, 'adminpanel/user_create.html', {
        'form': form,
        'user': user,
        'teams': teams,
        'projects': projects,
        'is_edit': True
    })

@login_required
@user_passes_test(is_admin)
def user_delete(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect('admin_panel:user_list')
    return render(request, 'adminpanel/user_confirm_delete.html', {'user': user})

def generate_random_password(length=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))


@login_required
@user_passes_test(is_admin)
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

@login_required
@user_passes_test(is_admin)
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})
