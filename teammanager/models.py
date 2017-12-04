from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Member(models.Model):
	ROLE_CHOICES = (
        (1, 'Regular'),
        (2, 'Admin'),
    )
	first_name  = models.CharField(max_length=30)
	last_name  = models.CharField(max_length=30)
	phoneno = models.CharField(max_length=40)
	email = models.CharField(max_length=200)
	role  = models.IntegerField(default=1) #{1:regular,2:admin}
