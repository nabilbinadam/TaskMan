from django.shortcuts import render,redirect
from .models import Item,Form,Task
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


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

def task_list_view(request): #get all data and return 

    task = Task.objects.all() # This take all object in the DB.




    return render(request, 'task_list_view.html',{'tasks':task}) 


from django.shortcuts import render
from .models import Task
from django.utils import timezone

def Time_Remaining(request, task_id):
    # Fetch the specific task by its ID
    task = Task.objects.get(id=task_id)

    # Get the current time
    current_time = timezone.now()  # Get the current date and time

    # Calculate the time remaining until the due date
    if task.DueDate:
        # Combine the due date with the minimum time to create a datetime object
        due_date = timezone.datetime.combine(task.DueDate, timezone.datetime.min.time())
        time_remaining = due_date - current_time  # Calculate the time remaining
    else:
        time_remaining = None  # Handle case where due date is not set

    return render(request, 'task_view_list.html', {'time_remaining': time_remaining})