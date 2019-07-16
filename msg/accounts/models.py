from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin,
)
from django.conf import settings
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
	
	def create_user(self, email, username, mobile, display_name=None, password=None):
		'''
		Raising ValueError for the user model
		'''
		if not email:
			raise ValueError("Users must have an email address")
		if not mobile:
			raise ValueError("Users must have an mobile number")
		if not display_name:
			display_name = username
			
		'''
		Making a new user instance which is stored in memory only...
		'''
		user = self.model(
			email = self.normalize_email(email),
			username = username,
			mobile = mobile,
			display_name = display_name,
		)
		user.set_password(password)
		user.save()
		return user
		

	def create_superuser(self, email, username, mobile, display_name, password):
		'''
		Here we pass the create_user() method above to create super_user
		'''
		user = self.create_user(
			email,
			username,
			mobile,
			display_name,
			password,
		)
		user.is_staff = True
		user.is_superuser = True
		user.save()
		return user
		
		
		
class User(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	mobile = models.IntegerField(unique=True)
	display_name = models.CharField(max_length=150)
	bio = models.CharField(max_length=150, blank=True, default="")
	avatar = models.ImageField(blank=True, null=True)
	date_joined = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	
	objects = UserManager()
	
	USERNAME_FIELD = "mobile"
	REQUIRED_FIELDS = ["email", "username", "display_name"]
	
	def __str__(self):
		return '@{}'.format(self.username)
	
	def get_short_name(self):
		return self.display_name
	
	def get_long_name(self):
		return '{} (@{})'.format(self.display_name, self.username)

		
		
		
		
		
		
		
		
		
		
		
		
		
		
		