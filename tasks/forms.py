from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
    title= forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Add new task...', 'class':'form-control mb-2 mr-sm-2 col-md-10'}))

    class Meta:
        model = Task
        fields = '__all__'