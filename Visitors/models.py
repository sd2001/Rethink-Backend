from django.db import models
from Admins.models import CreatePractioner
from datetime import datetime
from django.utils import timezone
import pytz
import uuid

class CheckSlots(models.Model):
    doctor_id = models.CharField(primary_key = True,editable = True, null=False, max_length=6)
    
    
    
    
    
    
    
    
    
    
    
    
    