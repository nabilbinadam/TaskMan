from django.db import IntegrityError
from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,Form,Task
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login 
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import logout



from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json


def item_list(request):
    return render(request,"item_list.html")


def form_input(request):
    if request.method == "POST":
        nm = request.POST.get("name")
        dsc = request.POST.get("description")

        if nm and dsc:
            data = Form(name=nm, description=dsc)
            data.save()
            return redirect('form')  # Redirect to item_list or another success page

    # Handle GET request and return the form template
    return render(request, "form.html")




def loginPage(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return redirect('login.html')  # Redirect to the login form if GET request
 

def login_view(request):

    return render(request,"login.html")

def create_signUp(request):
    if request.method == "POST":
        usr = request.POST.get('username')
        mail = request.POST.get('email')
        pas = request.POST.get('password')
        pass_confirm = request.POST.get('confirm_password')

        # Check email duplicate
        if User.objects.filter(email=mail).exists():
            messages.error(request, "User already exists with this email.")
            return redirect("/signUp/")

        
        elif pas == pass_confirm:
            
            new_user = User.objects.create_user(username=usr, email=mail, password=pas)
            new_user.save()

            messages.success(request, "User created successfully. You can log in now.")
            login(request, new_user)

            return redirect('dashboard')  

        else:
            messages.error(request, "Passwords do not match.")
            return redirect('signUp')


def signUp(request):

    return render(request,"signUp.html")

def logout_view(request):
    logout(request)  # Log out the user
    
    return redirect('home_view')



@login_required
def dashboard(request):


    return render(request,"dashboard.html")



@login_required
def create_task_view(request):
    if request.method == "POST":
        taskname = request.POST.get("task_name")
        desc = request.POST.get("task_description")
        date = request.POST.get("due_date")

        # Check that all fields are provided
        if taskname and desc and date:
            try:
                # Create a new Task instance and link it to the logged-in user
                task = Task(TaskName=taskname, Description=desc, DueDate=date, user=request.user)
                task.save()  # Save the task
                return redirect('task_list_view')  # Redirect to the task list view
            except IntegrityError:
                return render(request, 'create_task.html', {'error': 'An error occurred while creating the task.'})
        else:
            return render(request, 'create_task.html', {'error': 'All fields are required.'})

    return render(request, 'create_task.html')



@login_required

def task_list_view(request):
   
    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user)  # Filter tasks by the logged-in user
    else:
        tasks = Task.objects.none()  # Return an empty queryset if the user is not authenticated
    
    return render(request, 'task_list_view.html', {'tasks': tasks})



@login_required
def edit_task_view(request, task_id):
    # Retrieve the specific task using its ID
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        # Handle form submission
        task_name = request.POST.get("name")
        task_description = request.POST.get("description")

        if task_name and task_description:  # Validate input
            task.TaskName = task_name
            task.Description = task_description
            task.save()  # Save changes
            messages.success(request, "Task updated successfully!")
            return redirect('task_list_view')  # Redirect to task list

    # Prepare context with the entire task object
    context = {
        "task": task  # Pass the entire task object
    }

    # Render the edit template with the context
    return render(request, "edit.html", context=context)

@login_required
def delete_task_view(request,task_id):
   if request.method=="POST":
       task=get_object_or_404(Task, id=task_id)
       print(task)
       task.delete()
       return HttpResponse("Delete success")
    
   return redirect(request,"task_list_view.html")


def home_view(request):
    return render(request,"home.html")


def user_session(request):

    data = User.objectse