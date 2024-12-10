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


@csrf_exempt  # Use with caution; consider using CSRF tokens in production
@require_http_methods(["PUT"])
def edit_task_view(request,task_id):
    try:
        # Fetch the task by ID
        task = Task.objects.get(id=task_id)

        # Parse the JSON body
        body = json.loads(request.body)

        # Get values from the request body
        taskname = body.get("task_name")
        desc = body.get("task_description")
        date = body.get("due_date")

        # Update the task fields if provided
        if taskname is not None:
            task.TaskName = taskname
        if desc is not None:
            task.Description = desc
        if date is not None:
            task.DueDate = date

        # Save the updated task
        task.save()

        return JsonResponse({"success": True, "message": "Task updated successfully."}, status=200)

    except Task.DoesNotExist:
        return JsonResponse({"success": False, "message": "Task not found."}, status=404)
    except json.JSONDecodeError:
        return JsonResponse({"success": False, "message": "Invalid JSON."}, status=400)
    except Exception as e:
        return JsonResponse({"success": False, "message": str(e)}, status=500)
