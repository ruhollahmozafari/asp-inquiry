from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import serializers
from core.models import Inquiry, Device
from rest_framework import generics, status
from rest_framework.views import APIView
import json
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination


class LargeResultsSetPagination(pagination.PageNumberPagination):
    """
        pagination class
    """
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000


api_link = {
    'phone':{
        'Mobile':{
        'Hamrahavval':'https://core.inquiry.ayantech.ir/webservices/core.svc/MCIMobileBillInquiry',
        'Irancell':'https://core.inquiry.ayantech.ir/webservices/core.svc/MtnMobileBillInquiry',
        'Rightel':'https://core.inquiry.ayantech.ir/webservices/core.svc/RightelMobileBillInquiry',
        },
        'FixedLine':'https://core.inquiry.ayantech.ir/webservices/core.svc/FixedLineBillInquiry',
    },
    'car':'https://core.inquiry.ayantech.ir/webservices/core.svc/TrafficFinesInquiry',
    'home':{
        'ElectricityBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/ElectricityBillInquiry',
        'GasBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/GasBillInquiry',
        'WaterBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/WaterBillInquiry',
    }
}
    
def get_data(device):
    """
        the data( that the client intends to inquiry about ) that api received varies according to the device
        so this function give usthe address based on the advice
    """
    device_type = device.device_type

    if device_type == 'phone':
        return json.dumps({
                "Identity": {
                    "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
                    # "Token": "DB5529C5350449C8A71A87ACD6259172"
                },
                "Parameters": {
                    "MobileNumber": device.Number
                }
            })

    elif device_type == 'car':
        return json.dumps({
                "Identity": {
                    "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
                },
                "Parameters": {
                    "BarCode": device.BarCode
                }
            })

def change_mapping_data(device, data_dict):
    data_dict.update(data_dict.pop('Description', {}))
    data_dict.update(data_dict.pop('Status', {}))
    data_dict['device'] = device.id
    if not data_dict['Parameters'] == None:
        data_dict.update(data_dict.pop('Parameters', {}))
        if not data_dict['FinalTerm'] == None:
            FinalTerm_data = {"FinalTerm_" + str(key): val for key, val in data_dict['FinalTerm'].items()}
            data_dict.pop('FinalTerm')
            data_dict.update(FinalTerm_data)
        else:
            data_dict.pop('FinalTerm')

        if not data_dict['MidTerm'] == None:
            MidTerm_data = {"MidTerm_" + str(key): val for key, val in data_dict['MidTerm'].items()}
            data_dict.pop('MidTerm')
            data_dict.update(MidTerm_data)
        else:
            data_dict.pop('MidTerm')
            
    else:
        data_dict.pop('Parameters')
    
    return data_dict


def get_api_link(device):
    """
        api URL change according to the device that the client intends to inquiry about 
        so this function give usthe address based on the advice
    """
    device_type = device.device_type

    if device_type == 'phone':
        if device.TypeLine == 'Mobile':
            return api_link[device_type][device.TypeLine][device.Operator]
        else:
            return api_link[device_type][device.TypeLine]
    
    elif device_type == 'home':
        return api_link[device_type][device.bill_type]
    
    elif device_type == 'car':
        return api_link[device_type]



class BillInquiryApi(APIView):
    """
        create new inquiry for one of the client device
    """

    serializer_class = serializers.BillInquirySerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():

            header = {
                'Content-Type':'application/json',
                'Accept':'application/json',
                'Connection':'keep-alive',
                'User-Agent': 'PostmanRuntime/7.28.4',
                'Accept-Encoding':'gzip, deflate, br'
            }
            device = get_object_or_404(Device, pk=int(serializer.data['device']))
            data = get_data( device )
            api_link = get_api_link( device )
            response = requests.post(
                api_link,
                headers=header,
                data=data,
            )
            responsed_data = response.json()
            maped_data = change_mapping_data(device, responsed_data)

            if maped_data['Code'] == 'G00000':
                s = serializers.BillInquirySerializer(data=maped_data)
                s.save()


            return Response({'message': maped_data['Description']})
        
        else:
            return Response(
                serializer.errors,

                status=status.HTTP_400_BAD_REQUEST,)


class DeleteDevice(generics.DestroyAPIView):
    """
        Delete inquiry 
    """
    queryset = Device.objects.all()

    def get_object(self, queryset=None):
        device = Device.objects.get(pk=self.request.query_params['id'])
        return device

    def get(self, request, *args, **kwargs):
        device = self.get_object()
        device.delete()
        return Response("Inquiry deleted", status=status.HTTP_204_NO_CONTENT)


class UpdateDevice(generics.UpdateAPIView):
    """
        Update the inquiry 
    """
    queryset = Device.objects.all()

    def get_object(self, queryset=None):
        device = Device.objects.get(pk=self.request.query_params['id'])
        return device

    def post(self, request, *args, **kwargs):
        device = self.get_object()
        serializer = serializers.DeviceSerializer(device, data=request.data, partial=True)
        if serializer.is_valid():
            device = serializer.save()
            return Response(serializers.DeviceSerializer(device).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateDevice(generics.CreateAPIView):
    """
        Create the inquiry 
    """
    serializer_class = serializers.DeviceSerializer

    def create(self,request, *args, **kwargs):
        self.request.data['created_by'] = 1
        return super(CreateDevice, self).create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(created_by=1)


class ListDevice(generics.ListAPIView):
    """
        Retrieve inquiry
    """
    queryset = Device.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'device_type', 'is_active']
    ordering_fields = ['owner', 'device_type', 'is_active']
    serializer_class = serializers.DeviceSerializer
    pagination_class = LargeResultsSetPagination
    page_size = 2
    page_size_query_param = 'page_size'
    



