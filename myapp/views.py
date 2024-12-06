from django.shortcuts import render,redirect
from .models import Item,Form
from django.http import HttpResponse
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


