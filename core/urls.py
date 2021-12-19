from django.urls import path, include


from . import views

app_name = 'core'

urlpatterns = [

    path('irancel-mobile-bill-inquiry/', views.BillInquiryApi.as_view(), name='bill_inquiry'),


]