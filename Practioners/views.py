from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.response import Response
from Admins.models import CreatePractioner
from .models import Available, Slots
from .serializers import CreateSerializer, AvailableSerializer, SlotSerializer
import json
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
		
def makeslots(id,name,start_time,end_time):	
	start_date = datetime.datetime.now().date()
	end_date = datetime.datetime.now().date()
	days = []
	date = start_date
	while date <= end_date:
		hours = []
		time = datetime.datetime.strptime(start_time, '%H:%M')
		end = datetime.datetime.strptime(end_time, '%H:%M')
		while time <= end:
			hours.append(time.strftime("%H:%M"))
			time += datetime.timedelta(minutes=slot_time)
		date += datetime.timedelta(days=1)
		days.append(hours)

	slots = {}
	for hours in days:
		av = {}
		for h in hours:
			av[h] = False
		slots[datetime.date.today().strftime("%d-%m-%y")] = av
	slots = json.dumps(slots)
	return slots
class Availability(viewsets.ViewSet):
	def setTime(self, request):		
		serializer = AvailableSerializer(data = request.data)
		# d = serializer.data	
		# slot_val = makeslots(d.id, d.name, d.start_time, d.end_date)
		# # s_o = Slot()
		# slot_data = {
		# 	'id' : d.id,
		# 	'name': d.name,
		# 	'slots': slot_val,
		# }
		# slot_serial = SlotSerializer(slot_data)
		if serializer.is_valid():
			serializer.save()
			# slot_serial.save()
			return Response(serializer.data, status.HTTP_201_CREATED)
		return Response(status.HTTP_206_PARTIAL_CONTENT)
		# except Exception as e:
		# 	return Response(status = status.HTTP_406_NOT_ACCEPTABLE)

	def getTime(self, request, pk):
		try:
			det = Available.objects.get(id = pk)
			print(det, type(det))	
			serializer = AvailableSerializer(det)
			# print(serializer.data['name'], type(serializer.data['name']))
			return Response(serializer.data, status = status.HTTP_302_FOUND)
		except Exception:
			return Response(status = status.HTTP_404_NOT_FOUND)

	def UpdateTime(self, request, pk):
		try:
			det = Available.objects.get(id = pk)
			serializer = AvailableSerializer(instance = det, data = request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(d, status.HTTP_201_CREATED)
			return Response(status.HTTP_206_PARTIAL_CONTENT)
		except Exception as e:
			return Response(status = status.HTTP_404_NOT_FOUND) 


class SlotCheck(viewsets.ViewSet):
	def getSlots(self, request):
		try:			
			slots = Slots.objects.all()
			if slots is None:
				return HttpResponse(status = 404)				
			serializer = SlotSerializer(slots, many=True)
			return Response(serializer.data, status.HTTP_200_OK)
		except Exception:
			return Response(status = status.HTTP_404_NOT_FOUND) 
			
    

def home(request):
	return render(request, 'index.html')        
