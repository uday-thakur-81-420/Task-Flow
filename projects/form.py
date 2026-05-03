from django import forms
from .models import Project
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):
    members = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Project
        fields = ['name', 'description', 'members']