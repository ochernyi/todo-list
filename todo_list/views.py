from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic, View

from todo_list.forms import TaskForm
from todo_list.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "task_list"
    paginate_by = 10
    template_name = "todo_list/index.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:todo")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo_list:todo")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list:todo")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    paginate_by = 10


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo_list:tag-list")


class TaskSwitcher(View):

    @staticmethod
    def get(request, pk):
        task = Task.objects.get(id=pk)
        task.is_done = not task.is_done
        task.save()
        return HttpResponseRedirect(reverse_lazy("todo_list:todo"))
