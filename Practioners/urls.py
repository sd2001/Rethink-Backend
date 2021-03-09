from django.urls import path
from .views import Profile, Availability, home

urlpatterns = [
	path('', home, name = "index"),
 
	path('profile/<str:pk>', Profile.as_view({
    	'get': 'getProfile',
     	'put': 'updateProfile',
	}), name = "View and Update Profile"),
 
 	path('avail/<str:pk>', Availability.as_view({
		'put': 'UpdateTime',
		'get': 'getTime',		
	}), name = "View and update Time Slots"),
  
    path('avail', Availability.as_view({
		'post': 'setTime',
	}), name = "Setting Time")
	
]