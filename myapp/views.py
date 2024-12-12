from django.shortcuts import render,redirect,get_object_or_404
from .models import Item,Form,Task
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.utils import timezone

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

    #get input in html
    #check wether is in database
    #redirect

    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(request, username=username, password=password)


        if user not in None:
            login(request,user)
            return redirect('/dashboard')
        else:
            return render(request, 'loginpage.html', {'error': 'Invalid credentials'})


    return render(request,"login.html")


def signUp(request):
    if request.method == "POST":
        user= request.POST.get("username")
        email=request.POST.get("email")
        passw= request.POST.get("password")
        confirm_password = request.POST.get('confirm_password')


        if passw == confirm_password:
            
            try:
                user = object.create.user(user="username",email="email",passw="password",confirm_password="confirm_password")
                messages.succes(request,"Succes")
                return redirect(request,'login.html')
                
            except Exception as e:
                messages.error(request,str(e))
        else:
                messages.error(request,'passwor error')


    return render(request,"signUp.html")



def dashboard(request):


    return render(request,"dashboard.html")




def create_task_view(request):
    if request.method == "POST":
        taskname=request.POST.get("task_name")
        desc=request.POST.get("task_description")
        date=request.POST.get("due_date")

        if taskname and desc and date:
            data = Task(TaskName=taskname, Description=desc, DueDate=date)
            data.save()
            


    return render(request, 'create_task.html')  

def task_list_view(request):
    tasks = Task.objects.all()  # Get all tasks
    return render(request, 'task_list_view.html', {'tasks': tasks})





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


def delete_task_view(request,task_id):
   if request.method=="POST":
       task=get_object_or_404(Task, id=task_id)
       print(task)
       task.delete()
       return HttpResponse("Delete success")
    

   return redirect(request,"task_list_view.html")
