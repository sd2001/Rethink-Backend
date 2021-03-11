from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Register, RegisterVerify, Booking, PaymentVerify
from .serializers import R_Serializer, RV_Serializer, B_Serializer, BV_Serializer
from Rethink import settings
import uuid
# Create your views here.


class Register_Visitor(viewsets.ViewSet):
    def postVisitor(self, request):
        det = R_Serializer(data=request.data)
        if det.is_valid():
            det.save()
            otp = str(uuid.uuid4())[:5]
            ver = {
                'id': det.data['id'],
                'otp': otp
            }
            mssg = f"Hello {det.data['name']},\n Your OTP is {otp}."
            ver_serializer = RV_Serializer(data=ver)
            if ver_serializer.is_valid():
                send_mail("Verification OTP", mssg, settings.EMAIL_HOST_USER,[det.data['email']])
                ver_serializer.save()
            return Response(det.data, status = status.HTTP_201_CREATED)
        return Response(status.HTTP_206_PARTIAL_CONTENT)

    def getVisitor(self, request, pk):
        try:
            det = Register.objects.get(id=pk)
            # print(pk, type(pk))
            serializer = R_Serializer(det)
            # print(serializer.data, type(serializer))
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        except Exception:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def getAllVisitors(self, request):
        try:
            det = Register.objects.all()
            if det is None:
                return HttpResponse(status = 404)				
            serializer = R_Serializer(det, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception:
            return Response(status = status.HTTP_404_NOT_FOUND)
class Register_verify(viewsets.ViewSet):   
    def verified_registration(self, request):
        # try:
            vdata = request.data
            print(vdata['otp'], type(vdata))
            pk = uuid.UUID(vdata['id'])
            det = RegisterVerify.objects.get(id=pk)
            serializer = RV_Serializer(det)
            print(serializer.data['otp'], type(serializer))
            
            if str(vdata['otp']) == str(serializer.data['otp']):
                user = Register.objects.get(id=pk)
                user.verify = True
                user.save()
                u_serializer = R_Serializer(user)
                print(u_serializer.data)            
                return Response(status = status.HTTP_200_OK)	
            return Response(status = status.HTTP_406_NOT_ACCEPTABLE)
        # except Exception:
        #     return Response(status = status.HTTP_400_BAD_REQUEST)
    def getverify(self, request):
        # try:
            det = RegisterVerify.objects.all()
            if det is None:
                return HttpResponse(status = 404)				
            serializer = RV_Serializer(det, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        # except Exception:
        #     return Response(status = status.HTTP_404_NOT_FOUND)
    
    def get1verify(self, request, pk):
        try: 
            det = RegisterVerify.objects.get(id=uuid.UUID(pk))
            serializer = RV_Serializer(det)
            print(serializer.data, type(serializer))
            return Response(serializer.data, status=status.HTTP_302_FOUND)
        except Exception:
            return Response(status = status.HTTP_404_NOT_FOUND)       
        

def home(request):
    return render(request, 'index.html')
