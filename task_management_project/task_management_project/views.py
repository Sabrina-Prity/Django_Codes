from django.shortcuts import render, redirect
from task_model.models import TaskModel
from task_model.forms import TaskForm  

def home(request):
    tasks = TaskModel.objects.all()
    context = {'data': tasks}
    return render(request, 'home.html', context)

def edit(request, id):
    task = TaskModel.objects.get(pk=id) 
    task_form = TaskForm(instance=task) 

    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)  
        if task_form.is_valid():
            task_form.save() 
            return redirect('homepage')  

    return render(request, 'add_task.html', {'form': task_form})

def delete(request, id):
    post = TaskModel.objects.get(pk=id)  
    post.delete()  
    return redirect('homepage')  
