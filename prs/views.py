from django.shortcuts import render

# Create your views here.

def pr_list(request):
    """
    Render the PR list view.
    """
    return render(request, 'prs/pr_list.html')

def pr_create(request):
    """
    Render the PR create view.
    """
    return render(request, 'prs/pr_create.html')

def pr_detail(request, pr_id):
    """
    Render the PR detail view.
    """
    context = {
        'pr_id': pr_id
    }
    return render(request, 'prs/pr_detail.html', context)