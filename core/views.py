from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from . import serializers
from core.models import Phone
from rest_framework import generics, status
from rest_framework.views import APIView

import requests


# class IrancelMobileBillInquiryApi(generics.CreateAPIView):
#     queryset = IrancelMobileBillInquiry.objects.all()
#     serializer_class = IrancelMobileBillInquirySerializer


class IrancelMobileBillInquiryApi(APIView):
    serializer_class = serializers.BillInquirySerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            type_line = self.request.data['TypeLine']
            if type_line == 'Mobile':
                operator = self.request.data['operator']
                if operator == 'Irancell':
                    return serializers.IrancelMobileBillInquirySerializer
                elif operator == 'Hamrahavval':
                    return serializers.MtnMobileBillInquirySerializer
                elif operator == 'Rightel':
                    return serializers.MtnMobileBillInquirySerializer
                else:
                    return serializers.MobileBillInquirySerializer

            else:
                return serializers.FixedLineBillInquirySerializer

        elif self.request.method == 'GET':
            return serializers.MobileBillInquirySerializer
        else:
            return serializers.MobileBillInquirySerializer

    # def get(self, request, format=None):
    #
    #     return Response(data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            response = requests.post("https://core.inquiry.ayantech.ir/webservices/Core.svc/MtnMobileBillInquiry",json=serializer.data)
            data_dict = response.json()
            print(data_dict)
            data_dict["Number"] = serializer.data['MobileNumber']
            data_dict.update(data_dict.pop('Description', {}))
            data_dict.update(data_dict.pop('Status', {}))
            if not data_dict['Parameters'] == None:
                data_dict.update(data_dict.pop('Parameters', {}))
            else:
                data_dict.pop('Parameters')
            print("-----------------------------------------------")
            print(data_dict)
            print("-----------------------------------------------")
            m = Phone.objects.create(**data_dict)
            m.save()
            return Response({'message': data_dict['Parameters']})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,)
        # parameters = {
        #     "Identity": {
        #         "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
        #     },
        #     "Parameters": {
        #         "MobileNumber": "09376064697",
        #         "TraceNumber": "00000000000000000123456789"
        #     }
        # }
