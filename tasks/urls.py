from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('home/', views.collection_list_view, name='tasks_home'),
    path('<int:id>/', views.collection_detail_view, name='tasks_det'),
    path('<int:id>/edit/', views.collection_update_view, name='tasks_edit'),
    path('profile/', views.profile, name='profile'),
    path('create_tasks/', views.collection_create_view, name='create_tasks')
]
