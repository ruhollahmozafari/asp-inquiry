from django.contrib import admin
from .models import Phone
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ['Number','Description','last_inquiry', 'Code','Amount','PreviousDate', 'CurrentDate', 'PaymentDate', 'FullName', 'BillID', 'Operator','TypeLine']
    list_filter = ['Number',]
    # list_editable = []
