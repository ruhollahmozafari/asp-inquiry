from rest_framework import serializers
import json

from core.models import Phone



OPERATORS = [
    ('Irancell', 'Irancell'),
    ('Rightel', 'Rightel'),
    ('Hamrahavval', 'Hamrahavval'),
]
class MobileBillInquirySerializer(serializers.ModelSerializer):
    Operator = serializers.ChoiceField(choices=OPERATORS)
    MobileNumber = serializers.CharField(max_length=100)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []

class RightelMobileBillInquirySerializer(serializers.ModelSerializer):
    Amount = serializers.IntegerField(read_only=True)
    MobileNumber = serializers.CharField(max_length=100)
    PreviousDate = serializers.CharField(max_length=100)
    CurrentDate = serializers.CharField(max_length=100)
    PaymentDate = serializers.CharField(max_length=100)
    ExtraInfo = serializers.CharField(max_length=100)
    BillID = serializers.IntegerField()
    PaymentID = serializers.CharField(max_length=100)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []


class MtnMobileBillInquirySerializer(serializers.ModelSerializer):
    MobileNumber = serializers.CharField(max_length=100)
    Amount = serializers.IntegerField(read_only=True)
    ExtraInfo = serializers.CharField(max_length=100)
    BillID = serializers.IntegerField()
    PaymentID = serializers.CharField(max_length=100)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []


class IrancelMobileBillInquirySerializer(serializers.ModelSerializer):
    MobileNumber = serializers.CharField(max_length=100)
    TraceNumber = serializers.CharField(max_length=100, required=False)
    CurrentDate = serializers.CharField(max_length=100, required=False)
    Amount = serializers.IntegerField(read_only=True, required=False)
    paymentDate = serializers.CharField(max_length=100, required=False)

    class Meta:
        model = Phone
        # fields = '__all__'
        fields = ['MobileNumber','TraceNumber','CurrentDate','Amount','paymentDate',]

    def to_representation(self, instance):
        ret = super(IrancelMobileBillInquirySerializer, self).to_representation(instance)

        data = {
            "Identity": {
                "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
            },
            "Parameters": {
                "MobileNumber": ret.get('MobileNumber')
            }
        }
        return data



class FixedLineBillInquirySerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=100)
    FixedLineNumber = serializers.CharField(max_length=100)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []


TYPELINES = [
    ('FixedLine', 'FixedLine'),
    ('Mobile', 'Mobile'),
]

class BillInquirySerializer(serializers.ModelSerializer):
    Operator = serializers.ChoiceField(choices=OPERATORS)
    MobileNumber = serializers.CharField(max_length=100)
    TypeLine = serializers.ChoiceField(choices=TYPELINES)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []

    # def to_representation(self, instance):
    #     data = {
    #         "Identity": {
    #             "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
    #         },
    #         "Parameters": {
    #             "MobileNumber": self.MobileNumber
    #         }
    #     }
    #     return data