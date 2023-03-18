from django.urls import path

from todo_list.views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    switch_task_is_done,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="todo"),
    path("create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "task/<int:pk>/switch-task-is-done/",
        switch_task_is_done,
        name="switch-task-is-done",
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todo_list"
