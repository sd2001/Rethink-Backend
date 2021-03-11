from django.contrib import admin
from .models import Register, RegisterVerify, Booking, PaymentVerify

# Register your models here.
admin.site.register(Register)
admin.site.register(RegisterVerify)
admin.site.register(Booking)
admin.site.register(PaymentVerify)