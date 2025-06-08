"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin-panel/', include(('admin_panel.urls', 'admin_panel'), namespace='admin_panel')),
    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('teams/', include(('teams.urls', 'teams'), namespace='teams')),
    path('projects/', include(('projects.urls', 'projects'), namespace='projects')),
    path('tasks/', include(('tasks.urls', 'tasks'), namespace='tasks')),
    path('prs/', include(('prs.urls', 'prs'), namespace='prs')),
    path('', include(('core.urls', 'core'), namespace='core')), 
]

# Serve media/static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
