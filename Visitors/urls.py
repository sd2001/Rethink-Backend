from django.urls import path
from .views import Register_Visitor, Register_verify, home, BookingSlots


urlpatterns = [
	path('', home, name='index'),
	path('register', Register_Visitor.as_view({
        'post' : 'postVisitor',   
        'get' : 'getAllVisitors'      
     }), name='Registration as Visitor'),
 
	path('register/<uuid:pk>', Register_Visitor.as_view({
		'get' : 'getVisitor'
	}), name = "Fetch Registration Details" ),
 
	path('verify', Register_verify.as_view({
		'post' : 'verified_registration',
		'get' : 'getverify'
 	}), name = 'Make users verified'),
    
    path('verify/<str:pk>', Register_verify.as_view({
		'get' : 'get1verify'
 	}), name = 'Get user credentials'),
    
    path('bookslot', BookingSlots.as_view({
		'post' : 'postBooking',
		'get' : 'getBookings' 
	}), name = 'Booking Details'),
    
    path('bookverify', BookingSlots.as_view({
		'post' : 'pay_done' 
	}), name = 'Complete Payment')
 
]