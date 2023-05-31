from django.shortcuts import render
from .models import TodoList


def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/todo_list_list.html", context)

    # jen may 31    MU*ST MATCH NAMES FDLKJKRKT":P@#QR  #####SCREEN SHOTS@@######

    # IMPORTANT#
