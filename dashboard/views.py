from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tasks.models import Task
from projects.models import Project

@login_required
def dashboard(request):
    user = request.user
    is_admin = user.profile.is_admin()

    if is_admin:
        tasks = Task.objects.select_related('assigned_to', 'project').all()
        projects = Project.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user).select_related('project')
        projects = user.projects.all()

    total = tasks.count()
    done_count = tasks.filter(status='done').count()
    overall_progress = int((done_count / total) * 100) if total > 0 else 0
    overdue_tasks = [t for t in tasks if t.is_overdue()]

    context = {
        'total': total,
        'todo_count': tasks.filter(status='todo').count(),
        'inprogress_count': tasks.filter(status='in_progress').count(),
        'done_count': done_count,
        'overall_progress': overall_progress,
        'overdue_tasks': overdue_tasks,
        'recent_tasks': tasks.order_by('-created_at')[:10],
        'projects': projects,
        'is_admin': is_admin,
    }
    return render(request, 'dashboard/dashboard.html', context)