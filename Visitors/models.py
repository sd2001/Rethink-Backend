from django.db import models
from Admins.models import CreatePractioner
from datetime import datetime
from django.utils import timezone
import pytz
import uuid

class Register(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4(), editable=False)
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False, max_length=150)
    address = models.CharField(blank=False, max_length=100)
    postal = models.CharField(blank=False, max_length=10)
    city = models.CharField(blank=False, max_length=50)
    date = models.DateTimeField(auto_now=True , editable = False)
    state = models.CharField(blank=False, max_length=50)
    country = models.CharField(blank=False, max_length=50)
    nationality = models.CharField(blank=False, max_length=50)
    dob = models.CharField(blank=False, max_length=50)
    verify = models.BooleanField(default=False)
    
    def __str__(self):
        self.doc = self.name + " : " + str(self.verify) + "(" + str(self.id) + ")"
        return self.doc
    
class RegisterVerify(models.Model):
    id = models.UUIDField(primary_key=True, editable=True)
    otp = models.CharField(blank=False, max_length=5)
    
    def __str__(self):
        self.doc = str(self.id) + "/" + self.otp
        return self.doc
        
class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default = uuid.uuid4(), editable=False)
    patient_id = models.UUIDField(editable=True)
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(default="xyz@gmail.com" ,blank=False, max_length=150)
    dr_id = models.UUIDField(blank=False)
    slot = models.TimeField("Slot(hh:mm:ss)", blank=False)
    date = models.DateTimeField(auto_now=True , editable = False)
    choices  = (("video","video"), ("offline", "offline"), ("telephone","telephone"))
    mode = models.CharField(choices = choices, blank = False, max_length=30)
    payment = models.BooleanField(default=False)
    
    def __str__(self):
        self.doc = self.name + " - " + self.mode + " : " + str(self.slot)
        return self.doc
        
class PaymentVerify(models.Model):
    id = models.UUIDField(primary_key=True, editable=True)  
    name = models.CharField(blank=False, max_length=50)  
    patient_id = models.UUIDField(editable=True)      
    dr_id = models.UUIDField(editable=True)  
    amount = models.IntegerField()
    # otp = models.CharField(blank=False, max_length=5)

    
    def __str__(self):
        self.doc = self.name + " - " + str(self.amount)
        return self.doc    
    
    
    
    
    
    
    
    
    
    
    
    
    