from django.urls import path

from todo_list.views import TaskListView, TagListView, TaskCreateView, TagCreateView

urlpatterns = [
    path("", TaskListView.as_view(), name="todo"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
]

app_name = "todo_list"
