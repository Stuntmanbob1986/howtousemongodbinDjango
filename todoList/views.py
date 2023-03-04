from django.shortcuts import render

from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Todo List")

def index(response):
    return render(response, "todoList/todolist.html", {})

