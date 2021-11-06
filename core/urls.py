from django.urls import path
from core.views import (
		HomeView,UserHomeView
	)
from django.contrib.auth.decorators import login_required

urlpatterns=[
	path('',HomeView.as_view(),name='homepage'),
	path('lmb/dashboard/',login_required(UserHomeView.as_view()),name='user_feed_view'),


]