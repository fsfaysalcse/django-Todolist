from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import CreateNewList

# Create your views here.

def index(response,name):
    list = ToDoList.objects.get(name = name)
    items = list.item_set.get(id=1)
    return render(response,"main/base.html",{})

def home(response):
    return render(response,"main/home.html",{})

def create(response):
        if response.method == "POST":
            form = CreateNewList(response.POST)

            if form.is_valid():
                name = form.cleaned_data["name"]
                t = ToDoList(name=name)
                t.save()
        else:
            form = CreateNewList()    
        return render(response,"main/create.html",{"form":form})