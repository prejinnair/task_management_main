from django.shortcuts import render, get_object_or_404, redirect
from .models import Team
from .forms import TeamForm
from .decorators import is_admin
from django.contrib.auth.decorators import login_required, user_passes_test

@user_passes_test(is_admin)
def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

@user_passes_test(is_admin)
def team_create(request):
    form = TeamForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('teams:team_list')
    return render(request, 'teams/team_form.html', {'form': form})

@user_passes_test(is_admin)
def team_update(request, pk):
    team = get_object_or_404(Team, pk=pk)
    form = TeamForm(request.POST or None, instance=team)
    if form.is_valid():
        form.save()
        return redirect('teams:team_list')
    return render(request, 'teams/team_form.html', {'form': form})

@user_passes_test(is_admin)
def team_delete(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('teams:team_list')
    return render(request, 'teams/team_confirm_delete.html', {'team': team})

user_passes_test(is_admin)
def manage_team_members(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    if request.method == 'POST':
        # Handle adding or removing members
        if 'add_member' in request.POST:
            member_id = request.POST.get('member_id')
            if member_id:
                team.members.add(member_id)
        elif 'remove_member' in request.POST:
            member_id = request.POST.get('member_id')
            if member_id:
                team.members.remove(member_id)
        return redirect('teams:manage_team_members', team_id=team.id)
    return render(request, 'teams/manage_team_members.html', {'team': team})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'teams/team_detail.html', {'team': team})