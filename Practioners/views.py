from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from Admins.models import CreatePractioner
from .models import Available
from .serializers import CreateSerializer, AvailableSerializer
# Create your views here.
class Profile(viewsets.ViewSet):
	def getProfile(self, request, pk=None):
		try:
			det = CreatePractioner.objects.get(id = pk)
			print(det, type(det))
			serializer = CreateSerializer(det)
			return Response(serializer.data, status = status.HTTP_302_FOUND)
		except Exception:
			return Response(status = status.HTTP_404_NOT_FOUND)

	def updateProfile(self, request, pk=None):
		try:
			det = CreatePractioner.objects.get(id = pk)
			serializer = CreateSerializer(instance = det, data = request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status.HTTP_201_CREATED)
			return Response(status.HTTP_206_PARTIAL_CONTENT)
		except Exception as e:
			return Response(status = status.HTTP_404_NOT_FOUND)       
		
class Availability(viewsets.ViewSet):
	def setTime(self, request):
		try:
			serializer = AvailabilitySerializer(data= request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status.HTTP_201_CREATED)
			return Response(status.HTTP_206_PARTIAL_CONTENT)
		except Exception as e:
			return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

	def getTime(self, request, pk):
		try:
			det = Available.objects.get(id = pk)
			serializer = AvailableSerializer(det)
			return Response(serializer.data, status = status.HTTP_302_FOUND)
		except Exception:
			return Response(status = status.HTTP_404_NOT_FOUND)

	def UpdateTime(self, request, pk):
		try:
			det = Available.objects.get(id = pk)
			serializer = AvailableSerializer(instance = det, data = request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status.HTTP_201_CREATED)
			return Response(status.HTTP_206_PARTIAL_CONTENT)
		except Exception as e:
			return Response(status = status.HTTP_404_NOT_FOUND) 


def home(request):
	return render(request, 'index.html')        
