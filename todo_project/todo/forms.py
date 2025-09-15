from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'task', 'date_of_reminder', 'time_description']
        widgets = {
            'date_of_reminder': forms.DateInput(attrs={'type': 'date'}),
            'time_description': forms.TimeInput(attrs={'type': 'time'}),
        }
