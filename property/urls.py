from django.urls import path, include
from six import viewitems

from . import views

app_name = 'propety'

urlpatterns = [

    path('bill-inquiry/<int:device>', views.BillInquiryApi.as_view(), name='bill_inquiry'),
    path('delete-device-inquiry/<int:pk>', views.DeleteDevice.as_view(), name='delete_device_inquiry'),
    path('update-device-inquiry/<int:pk>', views.UpdateDevice.as_view(), name='update_device_inquiry'),
    path('create-device-inquiry/', views.CreateDevice.as_view(), name='create_device_inquiry'),
    path('list-device/', views.ListDevice.as_view(), name='list_device'),
    path('list-inquiry/', views.ListInquiry.as_view(), name='list_inquiry'),
    path('user_elastic_search/', views.UserAdvanceSearch.as_view(), ),

]

