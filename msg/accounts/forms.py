from django.contrib.auth.forms import UserCreationForm#
from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User



class UserCreateForm(UserCreationForm):
	class Meta:
		fields = ("username", "email", "mobile", "password1", "password2")
		model = get_user_model()
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].label = "choose your username"
		self.fields["email"].label = "your email address"