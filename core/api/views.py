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
                "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
            },
            "Parameters": {
                "MobileNumber": "09376064697",
                "TraceNumber": "00000000000000000123456789"
            }
        }

        response = requests.post("https://core.inquiry.ayantech.ir/webservices/Core.svc/MtnMobileBillInquiry", json=parameters)
        data_dict = response.json()
        data_dict["MobileNumber"] = "09376064697"
        data_dict.update(data_dict.pop('Description', {}))
        data_dict.update(data_dict.pop('Status', {}))
        if not data_dict['Parameters'] == None:
            data_dict.update(data_dict.pop('Parameters', {}))
        else:
            data_dict.pop('Parameters')
        print("-----------------------------------------------")
        print(data_dict)
        print("-----------------------------------------------")
        m = IrancelMobileBillInquiry(**data_dict)
        m.save()

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
