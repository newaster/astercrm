from django.db import models

# Create your models here.


class Software(models.Model):
	def __str__(self):
		return self.name 

	name = models.CharField(max_length=15,unique=True)
	url = models.CharField(max_length=50)
	feature_addon = models.CharField(max_length=30, default="None")
	module_addon = models.CharField(max_length=30,default="None")
