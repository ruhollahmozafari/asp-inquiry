from rest_framework import serializers
from core.models import IrancelMobileBillInquiry


class IrancelMobileBillInquirySerializer(serializers.ModelSerializer):
    # mobile = Mobileserializer(many=True)
    token = serializers.CharField(max_length=100)
    # MobileNumber
    traceNumber = serializers.CharField(max_length=100)
    currentDate = serializers.CharField(max_length=100)
    amount = serializers.IntegerField(read_only=True)
    paymentDate = serializers.CharField(max_length=100)

    class Meta:
        model = IrancelMobileBillInquiry
        fields = '__all__'
        # fields = []
