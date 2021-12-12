from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, TextInput, Textarea


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs={
                'id': 'form_username',
                'placeholder': 'Customer'
            }),
            'email': TextInput(attrs={
                'id': 'form_email',
                'placeholder': 'qwerty@gmail.com',
                'type': 'email'
            }),
            'password1': TextInput(attrs={
                'id': 'form_password',
                'type': 'password'
            }),
            'password2': TextInput(attrs={
                'id': 'form_password',
                'type': 'password'
            })
        }