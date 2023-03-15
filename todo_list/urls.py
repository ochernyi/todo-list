from django.urls import path

from todo_list.views import index

urlpatterns = [
    path("", index, name="todo")
]

app_name = "todo_list"
