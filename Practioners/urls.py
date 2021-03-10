from django.urls import path
from .views import Profile, Availability, home, SlotCheck

urlpatterns = [
	path('', home, name = "index"),
 
	path('profile/<uuid:pk>', Profile.as_view({
    	'get': 'getProfile',
     	'put': 'updateProfile',
	}), name = "View and Update Profile"),
 
 	path('avail/<uuid:pk>', Availability.as_view({
		'put': 'UpdateTime',
		'get': 'getTime',		
	}), name = "View and update Time Slots"),
  
    path('avail', Availability.as_view({
        'get': 'getAll',
		'post': 'setTime',
	}), name = "Setting Time"),
    
    path('slots', SlotCheck.as_view({
		'get': 'getSlots'
	}), name = "Getting Slot Details")
	
]