from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from chronos.models import Worker, Team


class TeamForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Team
        fields = "__all__"


class WorkerUpdatingForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ["username", "first_name", "last_name", "email", "position"]


class WorkerCreationForm(UserCreationForm):
    class Meta:
        model = Worker
        fields = ["username", "first_name", "last_name", "email", "position"]
