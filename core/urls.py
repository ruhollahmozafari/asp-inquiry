from django.urls import path, include


from . import views

app_name = 'core'

urlpatterns = [

    path('irancel-mobile-bill-inquiry/', views.IrancelMobileBillInquiryApi.as_view(), name='irancel_mobile_bill_inquiry'),


]