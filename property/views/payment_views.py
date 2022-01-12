from django.shortcuts import render

# Create your views here.
import logging
from azbankgateways.exceptions import AZBankGatewaysException
from django.http import HttpResponse, Http404
from django.urls import reverse
from azbankgateways import bankfactories, models as bank_models, default_settings as settings
# from django.utils.translation import gettext_lazy as _

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from django.views import View

from property.models.device_models import Inquiry

def go_to_gateway_view(request, amount, inquiry_id, phone_number=None):
# def go_to_gateway_view(request,phone_number=None):

    amount = amount
    # amount =100000
    if phone_number:
        user_mobile_number = str(phone_number)

    factory = bankfactories.BankFactory()
    try:
        bank = factory.auto_create()  # or factory.create(bank_models.BankType.BMI) or set identifier
        bank.set_request(request)
        bank.set_amount(amount)
        bank.set_inquiry_id(str(inquiry_id))

        # یو آر ال بازگشت به نرم افزار برای ادامه فرآیند
        bank.set_client_callback_url('/callback-gateway')
        if phone_number:
            bank.set_mobile_number(user_mobile_number)  # اختیاری

        # در صورت تمایل اتصال این رکورد به رکورد فاکتور یا هر چیزی که بعدا بتوانید ارتباط بین محصول یا خدمات را با این
        # پرداخت برقرار کنید.
        bank_record = bank.ready()

        # هدایت کاربر به درگاه بانک
        return bank.redirect_gateway()
    except AZBankGatewaysException as e:
        logging.critical(e)
        # TODO: redirect to failed page.
        raise e



def callback_gateway_view(request):
    tracking_code = request.GET.get(settings.TRACKING_CODE_QUERY_PARAM, None)
    if not tracking_code:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    inquiry_ID = bank_models.Bank.objects.get(tracking_code=tracking_code).inquiry_id
    current_inquiry = Inquiry.objects.get(id=int(inquiry_ID))

    try:
        bank_record = bank_models.Bank.objects.get(tracking_code=tracking_code)
    except bank_models.Bank.DoesNotExist:
        logging.debug("این لینک معتبر نیست.")
        raise Http404

    if bank_record.is_success:
        current_inquiry.payment_tracking_code = tracking_code
        current_inquiry.is_paid = True
        current_inquiry.save()

        return 200    # 'success_payment'

    # current_inquiry.is_paid = False
    # current_inquiry.order_base.save()
    return 400    # 'unsuccessful_payment'







# class Payment(APIView):
#     """
#         payment inquiry
#     """

#     def post(self, request, *args, **kwargs):
#         bill = get_object_or_404(Inquiry, pk=int(self.kwargs['inquiry_id']))
#         # response_payment = go_to_gateway_view(request, bill.get_total_cost() ,Inquiry.id ,request.user.phone_number) 
#         response_payment = go_to_gateway_view(request, bill.get_total_cost() ,Inquiry.id ) #TODO
#         if response_payment == 200:
#             return Response(status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

class Payment(View):
    """
        payment inquiry
    """

    def post(self, request, *args, **kwargs):
        bill = get_object_or_404(Inquiry, pk=int(self.kwargs['inquiry_id']))
        # response_payment = go_to_gateway_view(request, bill.get_total_cost() ,Inquiry.id ,request.user.phone_number) 
        return go_to_gateway_view(request, bill.get_total_cost() ,Inquiry.id ) #TODO