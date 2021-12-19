from rest_framework import serializers
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
    # mobile = Mobileserializer(many=True)
    token = serializers.CharField(max_length=100)
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
    # mobile = Mobileserializer(many=True)
    token = serializers.CharField(max_length=100)
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
    # mobile = Mobileserializer(many=True)
    token = serializers.CharField(max_length=100)
    MobileNumber = serializers.CharField(max_length=100)
    TraceNumber = serializers.CharField(max_length=100)
    CurrentDate = serializers.CharField(max_length=100)
    Amount = serializers.IntegerField(read_only=True)
    paymentDate = serializers.CharField(max_length=100)

    class Meta:
        model = Phone
        fields = '__all__'
        # fields = []

    def create(self, validated_data):
        parameters = {
            "Identity": {
                "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
            },
            "Parameters": {
                "MobileNumber": validated_data['MobileNumber']
            }
        }



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

