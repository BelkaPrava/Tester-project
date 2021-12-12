from django import forms
from .models import Task, Collection
from django.forms import ModelForm, TextInput, Textarea
from django.forms.models import (
    inlineformset_factory,
    formset_factory,
    modelform_factory,
    modelformset_factory
)


class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection
        fields = (
            'name',
            'description',
            'is_public'
        )
        widgets = {
            'name': TextInput(attrs={
                'class': 'module-create-form',
                'id': 'task-form-name',
            }),
            'description': Textarea(attrs={
                'class': 'module-create-form-area',
                'id': 'task-form-description'
            }),
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = (
            'name',
            'condition',
            'answer'
        )
        widgets = {
            'name': TextInput(attrs={
                'class': 'taskk-create-form',
            }),
            'description': Textarea(attrs={
                'class': 'taskk-create-form-area',
            }),
            'answer': TextInput(attrs={
                'class': 'taskk-create-form',
            }),
        }