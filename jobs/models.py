from django.db import models

# Create your models here.
class Job(models.Model):
	image_fun = models.ImageField(upload_to='images/', null=True)
	summary = models.CharField(max_length=200, null=True)
		