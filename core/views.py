from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class HomeView(View):
	template_name='core/homepage.html'

	def get(self,request):
		return render(request,self.template_name)

class UserHomeView(View):
	template_name='core/feed/feed3.html'

	def get(self,request):
		return render(request,self.template_name)