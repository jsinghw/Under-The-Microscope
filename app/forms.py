from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import CustomUser


class SignUpForm(UserCreationForm):
    display_name = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'display_name', 'password1', 'password2', )


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
