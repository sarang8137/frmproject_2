from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from .form import *
from django.views.generic import View,TemplateView,CreateView
from django.contrib import messages
from django.urls import reverse_lazy


# Create your views here.
class SignUp(CreateView):
    template_name="reg.html"
    model=User
    form_class=UserRegForm
    success_url=reverse_lazy('reg')
   