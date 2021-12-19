from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import IrancelMobileBillInquirySerializer
from core.models import IrancelMobileBillInquiry
from rest_framework import generics
from rest_framework.views import APIView

import requests


# class IrancelMobileBillInquiryApi(generics.CreateAPIView):
#     queryset = IrancelMobileBillInquiry.objects.all()
#     serializer_class = IrancelMobileBillInquirySerializer


class IrancelMobileBillInquiryApi(APIView):

    def get(self, request, format=None):
        parameters = {
            "Identity": {
                "Token": "String content"
            },
            "Parameters": {
                "MobileNumber": "String content",
                "TraceNumber": "String content"
            }
        }

        response = requests.get("https://core.inquiry.ayantech.ir/webservices/Core.svc/MtnMobileBillInquiry", params = parameters)
        print("-----------------------------------------------")
        print(response)
        print(response.json())

        print("-----------------------------------------------")
        return Response(response)

# @api_view(['GET', 'PUT', 'DELETE'])
# def irancel_mobile_bill_inquiry_api(request,pk):
#     try:
#         irancel_mobile = IrancelMobileBillInquiry.objects.get(id=pk)
#     except:
#         return Response(status=404)
#
#     if request.method == 'GET' :
#         res = dict()
#
#         return Response(res)
