from django.shortcuts import render

# Create your views here.

def task_list(request):
    """
    Render the task list view.
    """
    return render(request, 'tasks/task_list.html')

def task_kanban(request):
    """
    Render the task kanban view.
    """
    return render(request, 'tasks/task_kanban.html')

def task_create(request):
    """
    Render the task create view.
    """
    return render(request, 'tasks/task_create.html')

def task_detail(request, task_id):
    """
    Render the task detail view.
    """
    context = {
        'task_id': task_id
    }
    return render(request, 'tasks/task_detail.html', context)

def task_update(request, task_id):
    """
    Render the task update view.
    """
    context = {
        'task_id': task_id
    }
    return render(request, 'tasks/task_update.html', context)

