from django.urls import path
from .views import (
    index,
    ProjectListView,
    ProjectTaskListView,
    ProjectDetailView,
    ProjectCreateView,
    ProjectUpdateView,
    ProjectDeleteView,

    TaskListView,
    TaskDetailView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    toggle_assign_to_task,

    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,

    WorkerListView,
    WorkerDetailView,
    WorkerCreateView,
    WorkerUpdateView,
    WorkerDeleteView,

)


urlpatterns = [
    path("", index, name="index"),

    path(
        "projects/",
        ProjectListView.as_view(),
        name="project-list"
    ),
    path(
        "projects/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project-detail"
    ),
    path(
        "projects/<int:pk>/tasks/",
        ProjectTaskListView.as_view(),
        name="project-task-list"
    ),
    path(
        "projects/create/",
        ProjectCreateView.as_view(),
        name="project-create"
    ),
    path(
        "projects/<int:pk>/update/",
        ProjectUpdateView.as_view(),
        name="project-update"
    ),
    path(
        "projects/<int:pk>/delete/",
        ProjectDeleteView.as_view(),
        name="project-delete"
    ),

    path(
        "tasks/",
        TaskListView.as_view(),
        name="task-list"
    ),
    path(
        "tasks/<int:pk>/",
        TaskDetailView.as_view(),
        name="task-detail"
    ),
    path(
        "tasks/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
        "tasks/<int:pk>/toggle-assign/",
        toggle_assign_to_task,
        name="toggle-task-assign"
    ),

    path(
        "teams/",
        TeamListView.as_view(),
        name="team-list"
    ),
    path(
        "teams/<int:pk>/",
        TeamDetailView.as_view(),
        name="team-detail"
    ),
    path(
        "teams/create/",
        TeamCreateView.as_view(),
        name="team-create"
    ),
    path(
        "teams/<int:pk>/update/",
        TeamUpdateView.as_view(),
        name="team-update"
    ),
    path(
        "teams/<int:pk>/delete/",
        TeamDeleteView.as_view(),
        name="team-delete"
    ),

    path(
        "workers/",
        WorkerListView.as_view(),
        name="worker-list"
    ),
    path(
        "workers/<int:pk>/",
        WorkerDetailView.as_view(),
        name="worker-detail"
    ),
    path(
        "workers/create/",
        WorkerCreateView.as_view(),
        name="worker-create"
    ),
    path(
        "workers/<int:pk>/update",
        WorkerUpdateView.as_view(),
        name="worker-update"
    ),
    path(
        "workers/<int:pk>/delete",
        WorkerDeleteView.as_view(),
        name="worker-delete"
    ),
]

app_name = "chronos"
