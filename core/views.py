from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
# Create your views here.
@login_required
def dashboard_view(request):
    """
    Render the dashboard view.
    Redirect admin users to the admin dashboard.
    """
    user = request.user
    if user.is_superuser:
        return redirect('admin_panel:dashboard')
    else:
        return render(request, 'core/dashboard.html')

def about_view(request):
    """
    Render the about view.
    """
    return render(request, 'core/about.html')