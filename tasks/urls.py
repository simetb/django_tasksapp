from django.urls import path
from . import views

urlpatterns = [
    # Views
    path('home/', views.home_view ,name="home"),
    path('createTasks/', views.new_task ,name="createTasks"),
    path('editTask/<int:task_id>/', views.edit_task ,name="editTask"),
    path('deleteTask/<int:task_id>/', views.delete_task ,name="deleteTask"),
]