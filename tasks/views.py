from django.shortcuts import render
from .models import Task, Comment
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .form import TaskForm

@login_required
def task_list(request):
    user = request.user
    if user.profile.is_admin():
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST, user=request.user)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('dashboard')
    else:
        form = TaskForm(user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Create Task'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated!')
            return redirect('dashboard')
    else:
        form = TaskForm(instance=task, user=request.user)
    return render(request, 'tasks/task_form.html', {'form': form, 'title': 'Update Task'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.user.profile.is_admin():
        task.delete()
        messages.success(request, 'Task deleted.')
    return redirect('dashboard')

@login_required
def task_status_update(request, pk):
    # Drag-and-drop ya quick status change ke liye
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['todo', 'in_progress', 'done']:
            task.status = new_status
            task.save()
    return redirect('dashboard')

@login_required
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        # Status update
        new_status = request.POST.get('status')
        if new_status in ['todo', 'in_progress', 'done']:
            task.status = new_status
            if new_status == 'done':
                task.progress = 100
            elif new_status == 'todo':
                task.progress = 0
            task.save()
            messages.success(request, 'Status updated!')
            return redirect('task_detail', pk=pk)

        # Manual progress update
        manual_progress = request.POST.get('progress')
        if manual_progress is not None:
            task.progress = int(manual_progress)
            # Auto status update based on progress
            if task.progress == 100:
                task.status = 'done'
            elif task.progress > 0:
                task.status = 'in_progress'
            else:
                task.status = 'todo'
            task.save()
            messages.success(request, f'Progress updated to {task.progress}%!')
            return redirect('task_detail', pk=pk)

        # Comment add
        comment_text = request.POST.get('comment')
        if comment_text and comment_text.strip():
            Comment.objects.create(
                task=task,
                author=request.user,
                text=comment_text.strip()
            )
            messages.success(request, 'Comment added!')
            return redirect('task_detail', pk=pk)

    comments = task.comments.select_related('author').order_by('created_at')

    context = {
        'task': task,
        'comments': comments,
        'progress': task.progress,
    }
    return render(request, 'tasks/task_detail.html', context)