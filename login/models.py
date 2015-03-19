#-*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import UserManager
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.conf import settings
import os

#Create your models here.
class MyUserManager(BaseUserManager):
	def create_user(self, login, first_name, last_name, dob, email, mobile, password=None):
		user = self.model(email=self.normalize_email(email),
						  login = login,
						  first_name = first_name,
						  last_name = last_name,
						  dob = dob,
						  mobile = mobile,)
		user.set_password(password)
		user.save(using=self._db)
		return user

class UserModel(AbstractBaseUser):
	class Meta:
		db_table = "usermodel"

	login = models.CharField(max_length=30, unique=True)
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	dob = models.DateField()
	email = models.EmailField(unique=True)
	mobile = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[0-9]{3}-[0-9]{7}$',
                                        message='Неверный формат номера')], unique=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	avatar = models.ImageField(upload_to='%s/%Y/%m'.format(login), 
		 					   default='no_avatar.png',
		 					   blank=True,
		 					   null=True)
	REQUIRED = ['dob', 'mobile', 'last_name', 'email', 'first_name']
	USERNAME_FIELD = 'login'
	objects = MyUserManager()

	def get_short_name(self):
		return self.last_name + ' ' + self.first_name[:1] + '.'
