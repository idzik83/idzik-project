from django.db import models

# Create your models here.
class UserModel(models.Model):
	class Meta:
		db_table = "usermodel"

	usermodel_surname = models.CharField(max_length=30)
	usermodel_name =  models.CharField(max_length=30)
	usermodel_login = models.CharField(max_length=30)
	usermodel_password = models.CharField(max_length=30)
	usermodel_email = models.EmailField()
	usermodel_dob = models.DateField()
