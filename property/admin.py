from django.contrib import admin
from .models import Inquiry, Device


# Register your models here.
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner','name','is_active','description','last_inquiry',]
    list_filter = ['owner',]
    
@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['id', 'device','Description', 'Code','Amount','PreviousDate', 'CurrentDate', 'PaymentDate', 'FullName', 'BillID',]
    list_filter = ['device',]
    # list_editable = []

