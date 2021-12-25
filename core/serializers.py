from rest_framework import serializers
from core.models import Inquiry ,Device

class BillInquirySerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField()
    class Meta:
        model = Inquiry
        fields = '__all__'
        # fields = ['device','Description','Code','Amount','PreviousDate', 'CurrentDate', 'PaymentDate', 'FullName', 'BillID', 'device_id']


class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        fields = '__all__'
        # fields = ['Number', 'Operator','TypeLine','owner', 'name', 'last_inquiry', 'device_type', 'description']

