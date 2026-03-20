from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .models import Task
from .forms import TaskForm


@login_required
def task_list(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    tasks = Task.objects.filter(user=request.user, is_completed=False, is_deleted=False)
    return render(request, 'tasks/task_list.html', {'tasks': tasks, 'form': form})


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(user=request.user, is_completed=True, is_deleted=False)
    return render(request, 'tasks/completed.html', {'tasks': tasks})


@login_required
def deleted_tasks(request):
    tasks = Task.objects.filter(user=request.user, is_deleted=True)
    return render(request, 'tasks/deleted.html', {'tasks': tasks})


@login_required
@require_POST
def toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    next_url = request.POST.get('next', 'task_list')
    return redirect(next_url)


@login_required
@require_POST
def soft_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_deleted = True
    task.save()
    next_url = request.POST.get('next', 'task_list')
    return redirect(next_url)


@login_required
@require_POST
def restore_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.is_deleted = False
    task.save()
    return redirect('deleted_tasks')


@login_required
@require_POST
def permanent_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect('deleted_tasks')

