from django.shortcuts import render, redirect, get_object_or_404
from .models import TaskList, Task

def list_index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            TaskList.objects.create(name=name)
        return redirect('list_index')
    
    listas = TaskList.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'listas': listas})

def list_delete(request, list_id):
    lista = get_object_or_404(TaskList, id=list_id)
    lista.delete()
    return redirect('list_index')


def task_view(request, list_id):
    lista_obj = get_object_or_404(TaskList, id=list_id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            Task.objects.create(title=title, task_list=lista_obj)
        return redirect('task_view', list_id=list_id)

    tareas = lista_obj.tasks.all().order_by('completed', '-created_at')
    return render(request, 'tareas.html', {'lista': lista_obj, 'tareas': tareas})

def task_toggle(request, list_id, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    tarea.completed = not tarea.completed
    tarea.save()
    return redirect('task_view', list_id=list_id)

def task_delete(request, list_id, task_id):
    tarea = get_object_or_404(Task, id=task_id)
    tarea.delete()
    return redirect('task_view', list_id=list_id)