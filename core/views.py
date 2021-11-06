from django.shortcuts import render,redirect
from django.views.generic import View
from core.forms import ContactForm
from django.contrib.auth import authenticate
from django.contrib import messages
from core.models import Contact
# Create your views here.

class HomeView(View):
	template_name='core/homepage.html'

	def get(self,request):
		return render(request,self.template_name)

class UserHomeView(View):
	template_name='core/feed/feed3.html'

	def get(self,request):
		return render(request,self.template_name)

class ContactView(View):
	template_name='core/feed/contact.html'
	form_class=ContactForm
	

	def get(self,request):
		form=self.form_class()
		contact_list=Contact.objects.filter(email=request.user.email).all()[:3]
		context={'form':form,'contact_list':contact_list}
		return render(request,self.template_name,context)

	def post(self,request):
		form=self.form_class(request.POST)
		contact_list=Contact.objects.all()
		if form.is_valid():
			form.save()
			return redirect('contact_view')
			
		context={'form':form,'contact_list':contact_list}
		return render(request,self.template_name,context)