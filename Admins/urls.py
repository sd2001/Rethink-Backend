from django.urls import path
from .views import Manage_Clinic, home

urlpatterns = [
    path('', home, name = "index"),
	path('admin',  Manage_Clinic.as_view({
			'get':'get_practioners',
			'post':'post_practioners'}), name = 'Add a Practioner'),
]