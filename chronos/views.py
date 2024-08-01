from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .forms import TeamForm, WorkerCreationForm, WorkerUpdatingForm
from .models import Task, Team, Project, Worker


def index(request):
    return render(request, "chronos/index.html")


class ProjectListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project_list"
    template_name = "chronos/project_list.html"


class ProjectTaskListView(LoginRequiredMixin, generic.ListView):
    model = Project
    context_object_name = "project"
    template_name = "chronos/project_task_list.html"

    def get_queryset(self):
        return Project.objects.get(id=self.kwargs["pk"])


class ProjectDetailView(LoginRequiredMixin, generic.DetailView):
    model = Project


class ProjectCreateView(LoginRequiredMixin, generic.CreateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("chronos:project-list")


class ProjectUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Project
    fields = "__all__"
    success_url = reverse_lazy("chronos:project-list")


class ProjectDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Project
    success_url = reverse_lazy("chronos:project-list")


class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = "task_list"
    template_name = "chronos/task_list.html"
    paginate_by = 5
    ordering = ['deadline']

    SORT_CHOICES = [
        ("status", "Status"),
        ("deadline", "Deadline"),
        ("priority", "Priority"),
    ]
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]

    def get_queryset(self):
        sort_param = self.request.GET.get('sort', 'status')
        if sort_param not in [field[0] for field in self.SORT_CHOICES]:
            sort_param = 'status'

        status_param = self.request.GET.get('status', None)
        user_param = self.request.GET.get('user', None)

        queryset = Task.objects.all()

        if status_param:
            queryset = queryset.filter(status=status_param)

        if user_param:
            queryset = queryset.filter(assignees__username=user_param)

        queryset = queryset.order_by(sort_param)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sort_choices'] = self.SORT_CHOICES
        context['status_choices'] = self.STATUS_CHOICES
        context['current_sort'] = self.request.GET.get('sort', 'status')
        context['current_status'] = self.request.GET.get('status', None)
        context['current_user'] = self.request.GET.get('user', None)
        return context


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("chronos:project-detail")


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy(
            "chronos:task-detail", kwargs={'pk': self.object.pk}
        )


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task


class TeamListView(LoginRequiredMixin, generic.ListView):
    model = Team
    context_object_name = "team_list"
    template_name = "chronos/team_list.html"


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    model = Team


class TeamCreateView(LoginRequiredMixin, generic.CreateView):
    model = Team
    fields = "__all__"


class TeamUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Team
    form_class = TeamForm

    def get_success_url(self):
        return reverse_lazy(
            "chronos:team-detail", kwargs={'pk': self.object.pk}
        )


class TeamDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Team


class WorkerListView(LoginRequiredMixin, generic.ListView):
    model = Worker
    context_object_name = "worker_list"


class WorkerDetailView(LoginRequiredMixin, generic.DetailView):
    model = Worker
    template_name = "chronos/worker_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        worker = self.get_object()
        projects_assigned_to_worker = (
            Project.objects.filter(team__members=worker).distinct()
        )
        context["projects_assigned_to_worker"] = projects_assigned_to_worker
        return context


class WorkerCreateView(LoginRequiredMixin, generic.CreateView):
    model = Worker
    form_class = WorkerCreationForm
    success_url = reverse_lazy("chronos:worker-list")


class WorkerUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Worker
    form_class = WorkerUpdatingForm

    def get_success_url(self):
        return reverse_lazy(
            "chronos:team-detail", kwargs={'pk': self.object.pk}
        )


class WorkerDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Worker


@login_required
def toggle_assign_to_task(request, pk):
    worker = Worker.objects.get(id=request.user.id)
    if (
        Task.objects.get(id=pk) in worker.tasks_assigned.all()
    ):
        worker.tasks_assigned.remove(pk)
    else:
        worker.tasks_assigned.add(pk)
    return HttpResponseRedirect(reverse_lazy("chronos:task-detail", args=[pk]))
