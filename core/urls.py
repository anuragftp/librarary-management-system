from django.urls import path
from core.views import (
		HomeView,UserHomeView,ContactView
	)
from django.contrib.auth.decorators import login_required

urlpatterns=[
	path('',HomeView.as_view(),name='homepage'),
	path('lmb/dashboard/',login_required(UserHomeView.as_view()),name='user_feed_view'),
	path('lmb/contact_us/',login_required(ContactView.as_view()),name='contact_view'),


]