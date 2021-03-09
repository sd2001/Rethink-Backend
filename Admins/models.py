from django.db import models
from django.utils import timezone
from datetime import datetime, date
import pytz
import uuid

IST = pytz.timezone('Asia/Kolkata')
# Create your models here.
class CreatePractioner(models.Model):
    uid = "P"+str(uuid.uuid4())[:5]
    id = models.CharField(primary_key = True, default = uid, editable = False, max_length=6)
    name = models.CharField(max_length=100)
    picture_link = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    date_joined = models.DateField(default=timezone.now, editable = False)
    phone_number = models.IntegerField()
    available = models.BooleanField(default=False)
    PAN_number = models.CharField(max_length=10)
    Account_number = models.CharField(max_length=18)
    IFSC_number = models.CharField(max_length=11)
    
    def __str__(self):
        self.doc = self.name + "(" + self.specialization + ")" + "(" + self.id + ")"
        return self.doc
    
    