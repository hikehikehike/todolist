from django.views import generic
from django.urls import reverse_lazy
from todo_list.forms import TaskForm
from todo_list.models import Task, Tag
from django.http import HttpResponseRedirect


class TaskListViews(generic.ListView):
    model = Task
    fields = "__all__"


class TaskCreationViews(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskUpdateViews(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteViews(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


class TagsCreationViews(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags-list")


class TagsListViews(generic.ListView):
    model = Tag
    fields = "__all__"


class TagsUpdateViews(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tags-list")


class TagsDeleteViews(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tags-list")


def complete_undo(request, pk):
    task = Task.objects.get(pk=pk)
    task.done_or_not = not task.done_or_not
    task.save()
    return HttpResponseRedirect(reverse_lazy("todolist:task-list"))
