from django.contrib import admin
from .models import TodoList, TodoItem


class TodoListAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class TodoItemAdmin(admin.ModelAdmin):
    list_display = ("task", "due_date", "is_completed")


admin.site.register(TodoList, TodoListAdmin)
admin.site.register(TodoItem, TodoItemAdmin)


# test, do do list wasn't showing up in admin page  - #yeah this is what was missing!

# REMEMBER THIS SCOTT ^^^^^^^^^^^^^^^^^^^  ya dumb ass
