from django.shortcuts import render

# Create your views here.
def project_list(request):
    """
    Render the project list view.
    """
    return render(request, 'projects/project_list.html')

def project_create(request):
    """
    Render the project create view.
    """
    return render(request, 'projects/project_create.html')

def project_detail(request, project_id):
    """
    Render the project detail view.
    """
    context = {
        'project_id': project_id
    }
    return render(request, 'projects/project_detail.html', context)