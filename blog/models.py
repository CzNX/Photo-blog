from django.db import models

# Create your models here.

class My_Blog(models.Model):
	author = models.CharField(max_length =20)
	image = models.ImageField(upload_to='images')
	description = models.TextField()
	date_time = models.DateTimeField(auto_now_add=True, blank=True)


	def __str__(me):
		return me.author