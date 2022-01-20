from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from todo.models import Todo
from todo.forms import TodoForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
          
    return render(request, 'todo/reg.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/login.html', {'form': form})

@login_required(login_url='/login')
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='/login')
def index_view(request):
    if request.method == 'POST':
        title = request.POST['title']
        task = Todo(title = title, user = request.user)
        task.save() 
        
    tasks = Todo.objects.filter(user = request.user.id).order_by('-pub_date')
    print (tasks)
    return render(request, 'todo/index.html', {"tasks":tasks, "user":request.user})
    
@login_required(login_url='/login')
def complete_task(request, id):
    task = get_object_or_404(Todo, id=id)
    if task.user != request.user:
        return HttpResponse("Invalid action") 
    task.isDone = True
    task.done_date = datetime.now()
    task.save()
    return redirect('index') 

@login_required(login_url='/login')
def delete_task(request, id):
    task = get_object_or_404(Todo, id=id)
    if task.user != request.user:
        return HttpResponse("Invalid action") 
    task.delete()
    return redirect('index')