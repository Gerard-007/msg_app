from django.contrib.auth import login
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import FormView
# Create your views here.

class LoginView(FormView):
	form_class = AuthenticationForm
	success_url = reverse_lazy("posts:all")
	template_name = "accounts/login.html"
	
	def get_form(self, form_class=None):
		if form_class is None:
			form_class = self.get_form_class()
		return form_class(self.request, **self.get_form_kwargs())
	
	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)