from django.db import models
from Admins.models import CreatePractioner
from datetime import datetime
from django.utils import timezone
import pytz
import uuid

# IST = pytz.timezone('Asia/Kolkata')
# Create your models here.

class Available(models.Model):
    id = models.CharField(primary_key = True, editable = False,
                          max_length=6)
    name = models.CharField(default = "None", max_length=100)
    date = models.DateField(default=timezone.now, editable = False)
    start1 = models.TimeField("Start(hh:mm:ss)", blank=False)
    end1 = models.TimeField("End(hh:mm:ss)", blank=False)
    maxtime = models.IntegerField()
    
    def __str__(self):
        self.slots = f"{self.name}: ({self.start1} - {self.end1})"
        return self.slots
    
# class Appointment(models.Model):
    
class Slots(models.Model):
    id = models.CharField(primary_key = True, max_length=6)
    name = models.CharField(default = "None", max_length=100)
    date = models.DateField(default=timezone.now, editable = False)
    slots = models.JSONField(null = True)
    
    def __str__(self):
        return self.name

    