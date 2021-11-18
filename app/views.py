from django.contrib.auth import authenticate, logout
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser
from .forms import TodoForm
from .models import Todo
from django.contrib.auth.decorators import login_required
from main.settings import AUTH_PASSWORD_VALIDATORS

# Create your views here.


@login_required(login_url='login')
def home(request):
    form = TodoForm()
    user = request.user
    todos = Todo.objects.filter(user=user).order_by('priority')
    context = {
        'form' : form,
        'todos' : todos
    } 
    return render(request, 'index.html', context)

    

def login(request):
    if request.method == 'GET':
        form = AuthenticationForm(data=request.POST)
        context = {
        'form':form
        }
        return render(request, 'login.html',context)
    else:
        form =  AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                return redirect('home')
        else:
            context={
            'form':form
            }
            return render(request, 'login.html', context)


def signup(request):
    if request.method =='GET':
        form = UserCreationForm()
        context= {
        'form' : form
        }
        return render(request, 'signup.html', context)

    else:
        form = UserCreationForm(request.POST)
        context = {
            'form': form
        }
        if form.is_valid():
            user = form.save()
            if user is not None:
                return redirect('login')
        else:
            return render(request, 'signup.html', context)
  
    
@login_required(login_url='login')
def add_todo(request):

    if request.user.is_authenticated:
        user = request.user
        form =  TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            return redirect('home')
        else:
             return render(request, 'index.html', context={'form': form})


def delete_todo(request, id):
    Todo.objects.get(pk = id).delete()
    return redirect('home')


def status_todo(request, id, status):
    print(id)
    print(status)
    todo = Todo.objects.get(pk = id)
    todo.status=status
    todo.save()
    return redirect('home')


@login_required(login_url='login')
def signout(request):
    logout(request)
    return redirect('login')
    