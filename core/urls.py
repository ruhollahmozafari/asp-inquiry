from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [

    path('bill-inquiry/', views.BillInquiryApi.as_view(), name='bill_inquiry'),
    path('delete-device-inquiry/', views.DeleteDevice.as_view(), name='delete_device_inquiry'),
    path('update-device-inquiry/', views.UpdateDevice.as_view(), name='update_device_inquiry'),
    path('create-device-inquiry/', views.CreateDevice.as_view(), name='create_device_inquiry'),
    path('list-device/', views.ListDevice.as_view(), name='list_device'),

]
