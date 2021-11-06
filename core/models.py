from django.db import models
from crum import get_current_user

from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()
class Contact(models.Model):
	email=models.EmailField(max_length=50)
	user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
	description=models.CharField(max_length=300)
	reply=models.CharField(max_length=255)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.email)

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.user = user

		super(Contact, self).save(*args, **kwargs)
