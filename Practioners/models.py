from django.db import models
from Admins.models import CreatePractioner
from datetime import datetime
from django.utils import timezone
import pytz
import uuid

# IST = pytz.timezone('Asia/Kolkata')
# Create your models here.

class Available(models.Model):
    id = models.UUIDField(primary_key = True, default="YourID", editable = True,
                          max_length=36)
    name = models.CharField(default = "None", max_length=100)
    date = models.DateTimeField(auto_now=True , editable = False)
    start1 = models.TimeField("Start(hh:mm:ss)", blank=False)
    end1 = models.TimeField("End(hh:mm:ss)", blank=False)
    maxtime = models.IntegerField()
    
    def __str__(self):
        self.slots = f"{self.name}: ({self.start1} - {self.end1})"
        return self.name
    
# class Appointment(models.Model): 
class Slots(models.Model):
    id = models.UUIDField(primary_key = True, max_length=36)
    name = models.CharField(default = "None", max_length=100)
    date = models.DateField(auto_now_add=True, editable = False)
    slots = models.JSONField(null = True)
    
    def __str__(self):
        self.doc = self.name + "(" + str(self.id) + ")"
        return self.doc


    