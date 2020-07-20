from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	content=models.TextField()
	author=models.ForeignKey(User,on_delete=models.CASCADE)

	def __str__(self):
		return self.content

	def get_absolute_url(self):
		return reverse('post-detail',kwargs={'pk':self.pk})
