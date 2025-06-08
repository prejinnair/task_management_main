from django.shortcuts import render

# Create your views here.

def team_list(request):
    """
    Render the team list view.
    """
    return render(request, 'teams/team_list.html')

def team_create(request):
    """
    Render the team create view.
    """
    return render(request, 'teams/team_create.html')

def team_detail(request, team_id):
    """
    Render the team detail view.
    """
    context = {
        'team_id': team_id
    }
    return render(request, 'teams/team_detail.html', context)


def manage_team_members(request, team_id):
    """
    Render the manage team view.
    """
    context = {
        'team_id': team_id
    }
    return render(request, 'teams/manage_team.html', context)