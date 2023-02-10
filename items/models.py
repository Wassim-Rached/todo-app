from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=1000)
	done = models.BooleanField(default=False)
	owner = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)