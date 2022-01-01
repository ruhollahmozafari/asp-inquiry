from rest_framework import serializers
from .models import Inquiry ,Device

from django.contrib.auth import get_user_model

User = get_user_model()
# class BillInquirySerializer(serializers.ModelSerializer):
#     device_id = serializers.IntegerField()
#     class Meta:
#         model = Inquiry
#         fields = '__all__'
#         # fields = ['device','Description','Code','Amount','PreviousDate', 'CurrentDate', 'PaymentDate', 'FullName', 'BillID', 'device_id']

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class DeviceSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    created_by = UserSerializer()

    class Meta:
        model = Device
        fields = '__all__'
        depth = 2
        # fields = ['Number', 'Operator','TypeLine','owner', 'name', 'last_inquiry', 'device_type', 'description']


        
class BillInquirySerializer(serializers.ModelSerializer):
    # device = DeviceSerializer(required=False)
    # device_id = serializers.IntegerField()

    class Meta:
        model = Inquiry
        fields = '__all__'
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return { k: v for k, v in data.items() if v is not None }



import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents import DeviceDocument, InquiryDocument
class DeviceDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = DeviceDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'device_type',
            'MobileNumber',
            'FixedLineNumber',
            'BarCode',
            'ElectricityBillID',
            'ParticipateCode',
            'GasBillID',
            'WaterBillID',
        )


class InquiryDocumentSerializer(DocumentSerializer):
    """Serializer for the Book document."""

    class Meta:
        """Meta options."""

        # Specify the correspondent document class
        document = InquiryDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'PaymentID',
            'Description',
        )