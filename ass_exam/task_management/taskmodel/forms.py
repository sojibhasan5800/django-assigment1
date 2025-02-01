from django import forms
from .models import task_model

class task_form(forms.ModelForm):
    class Meta:
        model = task_model
        exclude ='is_completed'
        widgets = {
            'assign_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }