from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [

    path('bill-inquiry/', views.BillInquiryApi.as_view(), name='bill_inquiry'),
    path('delete-device-inquiry/', views.DeleteDevice.as_view(), name='delete_device_inquiry'),
    path('update-device-inquiry/', views.UpdateDevice.as_view(), name='update_device_inquiry'),
    path('retrieve-device-inquiry/', views.ListDevice.as_view(), name='retrieve_device_inquiry'),

]
