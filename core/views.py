from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import serializers
from core.models import Phone
from rest_framework import generics, status
from rest_framework.views import APIView
import json
import requests

api_operator_link = {
    'Mobile':{
        'Irancell':'https://core.inquiry.ayantech.ir/webservices/core.svc/MtnMobileBillInquiry',
        'Hamrahavval':'https://core.inquiry.ayantech.ir/webservices/core.svc/MCIExtendedBillInquiryRequestOtp',
        'Rightel':'https://core.inquiry.ayantech.ir/webservices/core.svc/RightelMobileBillInquiry',
    },
    'FixedLine':'https://core.inquiry.ayantech.ir/webservices/core.svc/FixedLineBillInquiry'
}
class BillInquiryApi(APIView):
    serializer_class = serializers.PhoneBillInquirySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # print(serializer.data['Number'])
            header = {
                'Content-Type':'application/json',
                'Accept':'application/json',
                'Connection':'keep-alive',
                'User-Agent':'PostmanRuntime/7.28.4',
                'Accept-Encoding':'gizp, deflate, br',
            }
            data = {
                "Identity": {
                    "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
                },
                "Parameters": {
                    "MobileNumber": serializer.data['Number']
                }
            }
            response = requests.post(
                api_operator_link[serializer.data['TypeLine']][serializer.data['Operator']],
                headers=header,
                data=json.dumps(data)
            )
            data_dict = response.json()
            data_dict["Number"] = serializer.data['Number']
            data_dict.update(data_dict.pop('Description', {}))
            data_dict.update(data_dict.pop('Status', {}))
            if not data_dict['Parameters'] == None:
                data_dict.update(data_dict.pop('Parameters', {}))
            else:
                data_dict.pop('Parameters')
            data_res = {**data_dict, **serializer.data}
            m = Phone(**data_res)
            m.save()
            return Response({'message': data_dict['Description']})
        else:
            return Response(
                serializer.errors,

                status=status.HTTP_400_BAD_REQUEST,)


# class InquiryDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     def retrieve(self, request, *args, **kwargs):
#         phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
#         serializer = serializers.PhoneSerializer(phone)
#         return Response(serializer.data)
#
#     def destroy(self, request, *args, **kwargs):
#         question = get_object_or_404(Phone, pk=kwargs.get('pk'))
#         question.delete()
#         return Response("Inquiry deleted", status=status.HTTP_204_NO_CONTENT)
#
#     def update(self, request, *args, **kwargs):
#         phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
#         serializer = serializers.PhoneSerializer(phone, data=request.data, partial=True)
#         if serializer.is_valid():
#             phone = serializer.save()
#             return Response(serializers.PhoneSerializer(phone).data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteInquiry(generics.RetrieveAPIView):
    queryset = Phone.objects.all()

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Phone, pk=kwargs.get('pk'))
        question.delete()
        return Response("Inquiry deleted", status=status.HTTP_204_NO_CONTENT)


class UpdateInquiry(generics.UpdateAPIView):
    queryset = Phone.objects.all()

    def get(self, request, *args, **kwargs):
        phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
        serializer = serializers.PhoneSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            phone = serializer.save()
            return Response(serializers.PhoneSerializer(phone).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveInquiry(generics.UpdateAPIView):
    queryset = Phone.objects.all()

    def get(self, request, *args, **kwargs):
        phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
        serializer = serializers.PhoneSerializer(phone)
        return Response(serializer.data)



    # def get_serializer_class(self):
    #     print("******************************************##########")
    #     if self.request.method == 'POST':
    #         print("******************************************")
    #         print(self.request.data)
    #         type_line = self.request.data['TypeLine']
    #
    #         if type_line == 'Mobile':
    #             operator = self.request.data['Operator']
    #             if operator == 'Irancell':
    #                 print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    #                 return serializers.IrancelMobileBillInquirySerializer
    #             elif operator == 'Hamrahavval':
    #                 return serializers.MtnMobileBillInquirySerializer
    #             elif operator == 'Rightel':
    #                 return serializers.MtnMobileBillInquirySerializer
    #             else:
    #                 return serializers.MobileBillInquirySerializer
    #
    #         else:
    #             return serializers.FixedLineBillInquirySerializer
    #
    #     elif self.request.method == 'GET':
    #         return serializers.BillInquirySerializer
    #     else:
    #         return serializers.PhoneBillInquirySerializer

    # def get(self, request, format=None):