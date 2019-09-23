from django.urls import path, include
from . import views

urlpatterns = [
	#paths that refer to the home and inform method
	path('', views.home, name='home'),
	path('inform', views.inform, name='inform')
  
]