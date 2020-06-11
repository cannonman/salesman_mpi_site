from django import forms
from django.contrib.auth.models import User
from salesman.models import Files
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]


class UploadFileForm(ModelForm):
    class Meta:
        model = Files
        fields = ('file', 'file_name',)
