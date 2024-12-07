from django.shortcuts import render,redirect
from .models import Item,Form
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
    return render(request, 'create_task.html')  

def task_list_view(request):
    return render(request, 'task_list_view.html') 