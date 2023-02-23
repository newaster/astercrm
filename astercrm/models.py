from django.db import models
from django.contrib.auth.models import User


class User_addon(models.Model):
	def __str__(self):
		na= self.user.username +"-"+self.role
		return na

	class Meta():
		unique_together = ('user', 'company_name')


			
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	mobileno = models.CharField(max_length=15)
	company_name = models.CharField(max_length=40)
	job_title = models.CharField(max_length=20)
	industry = models.CharField(max_length=20)
	location = models.CharField(max_length=20)
	discount = models.IntegerField()
	role = models.CharField(max_length=20)


class Software(models.Model):
	def __str__(self):
		return self.name 

	name = models.CharField(max_length=15)
	url = models.CharField(max_length=50)
	feature_addon = models.CharField(max_length=30, default="None")
	module_addon = models.CharField(max_length=30,default="None")

class Usage(models.Model):
	def __str__(self):
		return str(self.usage_user.first_name)+"--"+str(self.usage_software.name)

	class Meta():
		unique_together = ('usage_user', 'usage_software')

	usage_user = models.ForeignKey(User, on_delete=models.CASCADE)
	usage_software = models.ForeignKey(Software, on_delete=models.CASCADE)
	

class Sales(models.Model):
	def __str__(self):
		return str(self.usage_id.usage_user.first_name)+"--"+str(self.usage_id.usage_software.name)

	datetime=models.DateTimeField(auto_now_add=True)
	usage_id = models.ForeignKey(Usage,on_delete=models.CASCADE)
	price = models.IntegerField()
	sales_type = models.CharField(max_length=30)
	plant_smno=models.CharField(unique=True,max_length=15)


class Subscription(models.Model):
	def __str__(self):
		return str(self.usage_id.usage_software.name)+"--"+str(self.end_date)[:11]+"--"+str(self.status)

	plant_smno=models.CharField(unique=True,max_length=15)
	start_date=models.DateTimeField(auto_now_add=False)
	end_date=models.DateTimeField(auto_now=False)
	usage_id = models.ForeignKey(Usage,on_delete=models.CASCADE)
	price = models.IntegerField(default=1000)
	last_login = models.CharField(max_length=30,default="None")
	status = models.CharField(max_length=15,default="Active")
	

class Customer_Support(models.Model):
	def __str__(self):
		return str(self.subscription_id.usage_id.usage_software.name)+"--"+str(self.support_type) 

	datetime=models.DateTimeField(auto_now_add=True)
	subscription_id = models.ForeignKey(Subscription,on_delete=models.CASCADE)
	support_type = models.CharField(max_length=30)
	remark = models.CharField(max_length=130)











