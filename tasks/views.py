from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

# Create your views here.

# Views
# Ver las task del usuario
@login_required
def home_view(request):
    username =  request.user.username
    username = username.upper()
    user_tasks = Task.objects.filter(user=request.user)
    return render(request,'home.html',{'username':username,'tasks':user_tasks})

# Functions
# Create a new task
@login_required
def new_task(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        duration = request.POST['duration']
        user = request.user
        Task.objects.create(name=name, description=description, duration=duration, user=user)
        return redirect('home')
    
    else:
        return render(request, 'createTask.html')
    
# Edit a task 
@login_required   
def edit_task(request, task_id):
    
    task = get_object_or_404(Task, id=task_id)
            
    if task.user != request.user:
        return redirect('home')
    
    if(request.method == 'POST'):
        
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaskForm(instance=task)
        
    return render(request,'editTask.html',{'task': task})

# Delete Task
@login_required  
def delete_task(request, task_id):
    
    task = get_object_or_404(Task, id=task_id)
    
    if task.user != request.user:
        return redirect('home')
    
    task.delete()
    
    return redirect('home')
        

