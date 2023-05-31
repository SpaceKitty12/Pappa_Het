from django.contrib import admin
from .models import TodoList


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(
    TodoList, TodoListAdmin
)  # test, do do list wasn't showing up in admin page  - #yeah this is what was missing!

# REMEMBER THIS SCOTT ^^^^^^^^^^^^^^^^^^^  ya dumb ass
