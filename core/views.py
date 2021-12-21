from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import serializers
from core.models import Inquiry, Device
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

# def merge_two_dicts(x, y):
#     z = x.copy()   
#     z.update(y)    
#     return z

def determine_device(device_ID):
    device = get_object_or_404(Device, pk=int(device_ID))
    return device
    
def get_data(device):
    device_type = device.device_type

    if device_type == 'phone':
        return {
                "Identity": {
                    "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
                },
                "Parameters": {
                    "MobileNumber": device.Number
                }
            }

def get_api_operator_link(device):
    device_type = device.device_type

    if device_type == 'phone':
        return api_operator_link[device.TypeLine][device.Operator]


class BillInquiryApi(APIView):
    serializer_class = serializers.BillInquirySerializer

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
            print(serializer.data)
            device = determine_device( serializer.data['device_id'] )
            data = get_data( device )
            api_link = get_api_operator_link( device )

            response = requests.post(
                api_link,
                headers=header,
                data=json.dumps(data)
            )
            data_dict = response.json()
            data_dict["Number"] = device.Number 
            data_dict.update(data_dict.pop('Description', {}))
            data_dict.update(data_dict.pop('Status', {}))

            if not data_dict['Parameters'] == None:
                data_dict.update(data_dict.pop('Parameters', {}))
            else:
                data_dict.pop('Parameters')

            print(data_dict)
            # data_res = merge_two_dicts( device_data ,data_dict)
            # print(data_res)

            if data_dict['Code'] == 'G00000':
                m = Inquiry(device)
                m.update(**data_dict)
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
    queryset = Device.objects.all()

    def get(self, request, *args, **kwargs):
        question = get_object_or_404(Phone, pk=kwargs.get('pk'))
        question.delete()
        return Response("Inquiry deleted", status=status.HTTP_204_NO_CONTENT)


class UpdateInquiry(generics.UpdateAPIView):
    queryset = Device.objects.all()

    def get(self, request, *args, **kwargs):
        phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
        serializer = serializers.DeviceSerializer(phone, data=request.data, partial=True)
        if serializer.is_valid():
            phone = serializer.save()
            return Response(serializers.PhoneSerializer(phone).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetrieveInquiry(generics.UpdateAPIView):
    queryset = Device.objects.all()

    def get(self, request, *args, **kwargs):
        phone = get_object_or_404(Phone, pk=kwargs.get('pk'))
        serializer = serializers.DeviceSerializer(phone)
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