from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/completed/', views.completed_tasks, name='completed_tasks'),
    path('tasks/deleted/', views.deleted_tasks, name='deleted_tasks'),
    path('tasks/<int:pk>/toggle/', views.toggle_complete, name='toggle_complete'),
    path('tasks/<int:pk>/delete/', views.soft_delete, name='soft_delete'),
    path('tasks/<int:pk>/restore/', views.restore_task, name='restore_task'),
    path('tasks/<int:pk>/permanent-delete/', views.permanent_delete, name='permanent_delete'),
]
