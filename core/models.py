from django.db import models
from crum import get_current_user

from django.contrib.auth import get_user_model

# Create your models here.

RETURN_CHOICES = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

User = get_user_model()

class Student(models.Model):
	name=models.CharField(max_length=100)
	department=models.CharField(max_length=100)
	user=models.OneToOneField(User,related_name='student_reg',on_delete=models.CASCADE,null=True)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.user = user

		super(Student, self).save(*args, **kwargs)

class Teacher(models.Model):
	name=models.CharField(max_length=100)
	user=models.OneToOneField(User,related_name='teacher_reg',on_delete=models.CASCADE,null=True)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.name)

	def save(self, *args, **kwargs):
		user = get_current_user()
		if user and not user.pk:
			user = None
		if not self.pk:
			self.user = user

		super(Teacher, self).save(*args, **kwargs)


class Book(models.Model):
	name=models.CharField(max_length=150)
	author=models.CharField(max_length=100)
	publication=models.CharField(max_length=200)
	publication_year=models.DateTimeField()
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.name)

class BookIssue(models.Model):
	sudent=models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
	book=models.ForeignKey(Book,on_delete=models.CASCADE,null=True)
	penality=models.IntegerField(default=0)
	book_return=models.CharField(max_length=50,choices=RETURN_CHOICES,null=True,blank=True)
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)


	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.student)

class Event(models.Model):
	event_name=models.CharField(max_length=100)
	event_description=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.event_name)

class Due(models.Model):
	book_issue=models.ForeignKey(BookIssue,on_delete=models.CASCADE,null=True)
	payment=models.IntegerField()
	created_on=models.DateTimeField(auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']

	def __str__(self):
		return str(self.book_issue)




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
