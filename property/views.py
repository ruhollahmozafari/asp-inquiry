from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from . import serializers
from .models import Inquiry, Device
from rest_framework import generics, status
from rest_framework.views import APIView
import json
import requests
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination
from django.utils import timezone

class LargeResultsSetPagination(pagination.PageNumberPagination):
    """
        pagination class
    """
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            # 'links': {
            #    'next': self.get_next_link(),
            #    'previous': self.get_previous_link()
            # },
            'count': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })




class BillInquiryApi(APIView):
    """
        create new inquiry for one of the client device
    """

    serializer_class = serializers.BillInquirySerializer

    TOKEN = "3074B060C52E440BABC2BAAA4FF9A8E5"
    # TOKEN = "DB5529C5350449C8A71A87ACD6259172"

    api_link = {
        'Hamrahavval':'https://core.inquiry.ayantech.ir/webservices/core.svc/MCIMobileBillInquiry',
        'Irancell':'https://core.inquiry.ayantech.ir/webservices/core.svc/MtnMobileBillInquiry',
        'Rightel':'https://core.inquiry.ayantech.ir/webservices/core.svc/RightelMobileBillInquiry',
        'FixedLine':'https://core.inquiry.ayantech.ir/webservices/core.svc/FixedLineBillInquiry',
        'car':'https://core.inquiry.ayantech.ir/webservices/core.svc/TrafficFinesInquiry',
        'ElectricityBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/ElectricityBillInquiry',
        'GasBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/GasBillInquiry',
        'WaterBill':'https://core.inquiry.ayantech.ir/webservices/core.svc/WaterBillInquiry',
    }


    def change_mapping_data(self, device, data_dict):
        data_dict.update(data_dict.pop('Description', {}))
        data_dict.update(data_dict.pop('Status', {}))
        data_dict['device'] = device.id
        if not data_dict['Parameters'] == None:
            data_dict.update(data_dict.pop('Parameters', {}))
            if 'FinalTerm' in data_dict.keys():
                if not data_dict['FinalTerm'] == None:
                    FinalTerm_data = {"FinalTerm_" + str(key): val for key, val in data_dict['FinalTerm'].items()}
                    data_dict.pop('FinalTerm')
                    data_dict.update(FinalTerm_data)
                else:
                    data_dict.pop('FinalTerm')
            if 'MidTerm' in data_dict.keys():
                if not data_dict['MidTerm'] == None:
                    MidTerm_data = {"MidTerm_" + str(key): val for key, val in data_dict['MidTerm'].items()}
                    data_dict.pop('MidTerm')
                    data_dict.update(MidTerm_data)
                else:
                    data_dict.pop('MidTerm')
                
        else:
            data_dict.pop('Parameters')
        
        return data_dict
    
    def get_data(self, device):
        """
            the data( that the client intends to inquiry about ) that api received varies according to the device
            so this function give usthe address based on the advice
        """
        device_type = device.device_type

        if device_type == 'Irancell' or device_type == 'Hamrahavval' or device_type == 'Rightel':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "MobileNumber": device.MobileNumber
                    }
                })

        elif device_type == 'FixedLine':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "FixedLineNumber": device.FixedLineNumber
                    }
                })

        elif device_type == 'car':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "BarCode": device.BarCode
                    }
                })
        
        elif device_type == 'ElectricityBill':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "ElectricityBillID": device.ElectricityBillID
                    }
                })
        
        elif device_type == 'GasBill':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "ParticipateCode": device.ParticipateCode,
                        "GasBillID": device.GasBillID
                    }
                })
        
        elif device_type == 'WaterBill':
            return json.dumps({
                    "Identity": {
                        "Token": self.TOKEN
                    },
                    "Parameters": {
                        "WaterBillID": device.WaterBillID
                    }
                })


    def post(self, request, *args, **kwargs):
        header = {
            'Content-Type':'application/json',
            'Accept':'application/json',
            'Connection':'keep-alive',
            'User-Agent': 'PostmanRuntime/7.28.4',
            'Accept-Encoding':'gzip, deflate, br'
        }
        device = get_object_or_404(Device, pk=int(self.kwargs['device']))
        data = self.get_data( device )
        response = requests.post(
            self.api_link[device.device_type],
            headers=header,
            data=data,
        )
        responsed_data = response.json()
        maped_data = self.change_mapping_data(device, responsed_data)

        if maped_data['Code'] == 'G00000':
            s = serializers.BillInquirySerializer(data=maped_data)
            if s.is_valid():
                s.save()
                device.last_inquiry = timezone.now()
                device.save()
            else:
                s.errors


        return Response(maped_data)
    



class DeleteDevice(generics.DestroyAPIView):
    """
        Delete Device 
    """
    serializer_class = serializers.DeviceSerializer
    queryset = Device.objects.all()

    def get_object(self, queryset=None):
        # device = Device.objects.get(pk=self.request.query_params['id'])
        device = Device.objects.get(pk=self.kwargs['pk'])
        return device

    def destroy(self, request, *args, **kwargs):
        device = self.get_object()
        device.is_active = False
        device.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateDevice(generics.UpdateAPIView):
    """
        Update the Device 
    """
    serializer_class = serializers.DeviceSerializer
    queryset = Device.objects.all()

    def get_object(self, queryset=None):
        # device = Device.objects.get(pk=self.request.query_params['id'])
        device = Device.objects.get(pk=self.kwargs['pk'])
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
        Create the Device 
    """
    serializer_class = serializers.DeviceSerializer

    def create(self,request, *args, **kwargs):
        self.request.data['created_by'] = 1
        return super(CreateDevice, self).create(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(created_by=1)


class ListDevice(generics.ListAPIView):
    """
        Retrieve Devices
    """
    queryset = Device.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['owner', 'device_type', 'is_active',]
    ordering_fields = ['owner', 'device_type', 'is_active']
    serializer_class = serializers.DeviceSerializer
    pagination_class = LargeResultsSetPagination
    page_size = 2
    page_size_query_param = 'page_size'
    

class ListInquiry(generics.ListAPIView):
    """
        Retrieve inquiries
    """
    queryset = Inquiry.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['device',]
    ordering_fields = ['device',]
    serializer_class = serializers.BillInquirySerializer
    pagination_class = LargeResultsSetPagination
    page_size = 2
    page_size_query_param = 'page_size'






from django_elasticsearch_dsl_drf.constants import (
    LOOKUP_FILTER_TERMS,
    LOOKUP_FILTER_RANGE,
    LOOKUP_FILTER_PREFIX,
    LOOKUP_FILTER_WILDCARD,
    LOOKUP_QUERY_IN,
    LOOKUP_QUERY_GT,
    LOOKUP_QUERY_GTE,
    LOOKUP_QUERY_LT,
    LOOKUP_QUERY_LTE,
    LOOKUP_QUERY_EXCLUDE,
)
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import DeviceDocument, InquiryDocument
from .serializers import DeviceDocumentSerializer, InquiryDocumentSerializer


class DeviceDocumentView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = DeviceDocument
    serializer_class = DeviceDocumentSerializer
    pagination_class = LargeResultsSetPagination
    lookup_field = 'id'
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        
        'device_type',
        'MobileNumber',
        'FixedLineNumber',
        'BarCode',
        'ElectricityBillID',
        'ParticipateCode',
        'GasBillID',
        'WaterBillID',
    )
    # Define filter fields
    filter_fields = {
        # "properties": {
        "device_type": { 
        "type":     "text",
        "fielddata": True
        }
        # }
    }
        
        

    # Define ordering fields
    ordering_fields = {
        
        'device_type': 'device_type',
    }
    # Specify default ordering
    ordering = ( 'device_type', )