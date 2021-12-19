from django.urls import path, include

from . import views

app_name = 'core'

urlpatterns = [

    path('bill-inquiry/', views.BillInquiryApi.as_view(), name='bill_inquiry'),
    path('delete-bill-inquiry/', views.DeleteInquiry.as_view(), name='delete_bill_inquiry'),
    path('update-bill-inquiry/', views.UpdateInquiry.as_view(), name='update_bill_inquiry'),
    path('retrieve-bill-inquiry/', views.RetrieveInquiry.as_view(), name='retrieve_bill_inquiry'),

]
