from django.urls import path
from . import views

app_name = 'prs'

urlpatterns = [
    path('', views.pr_list, name='pr_list'),
    path('create/', views.pr_create, name='pr_create'),
    path('<int:pr_id>/', views.pr_detail, name='pr_detail'),
]
