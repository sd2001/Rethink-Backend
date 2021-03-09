from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import CreatePractioner
from .serializers import CreateSerializer
# Create your views here.

class Manage_Clinic(viewsets.ViewSet):
	def get_practioners(self,request):   
		if request.method == 'GET': 
			practioners = CreatePractioner.objects.all()
			if practioners is None:
				return HttpResponse(status = 404)
				
			serializer =CreateSerializer(practioners, many=True)
			return Response(serializer.data)
		return HttpResponse(status = 404)

	def post_practioners(self,request):	
		# try:	
		serializer =CreateSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(status.HTTP_206_PARTIAL_CONTENT)
		# except Exception as e:
		# 	return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
        
    
def home(request):
    return render(request, 'index.html')
    
    