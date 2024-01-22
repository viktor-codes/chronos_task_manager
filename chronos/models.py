from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


class Position(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=55)
    members = models.ManyToManyField("Worker", related_name="teams")

    def __str__(self):
        return f"{self.name}: {self.members}"

    def get_absolute_url(self):
        return reverse("chronos:team-detail", kwargs={'pk': self.pk})


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE,
        null=True, blank=True
    )
    groups = models.ManyToManyField(
        Group, blank=True, related_name='workers_group'
    )
    user_permissions = models.ManyToManyField(
        Permission, blank=True, related_name='workers_permission'
    )

    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class TaskType(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name="projects",
        blank=True, null=True
    )

    def __str__(self):
        return self.name


class Task(models.Model):

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    title = models.CharField(max_length=55)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="Pending"
    )
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default="Low"
    )
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    assignees = models.ManyToManyField(
        Worker, related_name="tasks_assigned"
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="tasks"
    )

    def __str__(self):
        return self.title
