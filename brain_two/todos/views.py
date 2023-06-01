from django.shortcuts import get_object_or_404, render
from .models import TodoList, TodoItem
from django.shortcuts import redirect


def todo_list_list(request):
    todo_lists = TodoList.objects.all()
    context = {"todo_lists": todo_lists}
    return render(request, "todos/todo_list_list.html", context)


def todo_list_detail(request, id):
    todo_list = get_object_or_404(TodoList, id=id)
    tasks = TodoItem.objects.filter(list=todo_list)
    return render(
        request,
        "todos/todo_list_detail.html",
        {"todo_list": todo_list, "tasks": tasks},
    )

    # jen may 31    MU*ST MATCH NAMES FDLKJKRKT":P@#QR  #####SCREEN SHOTS@@######### come crawling fasterrrrrrrrr, #your lyric here.  YOUR LIFE BURNS FASTERRRRRR. your lyric hereman

    # IMPORTANT#


def create_todo_list(request):
    if request.method == "POST":
        form = TodoListForm(request.POST)
        if form.is_valid():
            list = form.save()
            return redirect("todo_list_detail", id=list.id)
