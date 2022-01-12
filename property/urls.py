from django.urls import path, include

from .views import device_views ,payment_views

app_name = 'property'

urlpatterns = [

    path('bill-inquiry/<int:device>', device_views.BillInquiryApi.as_view(), name='bill_inquiry'),
    path('delete-device-inquiry/<int:pk>', device_views.DeleteDevice.as_view(), name='delete_device_inquiry'),
    path('update-device-inquiry/<int:pk>', device_views.UpdateDevice.as_view(), name='update_device_inquiry'),
    path('create-device-inquiry/', device_views.CreateDevice.as_view(), name='create_device_inquiry'),
    path('list-device/', device_views.ListDevice.as_view(), name='list_device'),
    path('list-inquiry/', device_views.ListInquiry.as_view(), name='list_inquiry'),

    path('go-to-gateway/', payment_views.go_to_gateway_view, name='go-to-gateway'),
    path('callback-gateway/', payment_views.callback_gateway_view, name='callback-gateway'),
    path('payment/<int:inquiry_id>', payment_views.Payment.as_view(), name='payment'),

]
