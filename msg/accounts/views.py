from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
# Create your views here.

class LoginView(FormView):
	form_class