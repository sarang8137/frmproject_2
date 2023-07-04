from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserRegForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields="__all__"