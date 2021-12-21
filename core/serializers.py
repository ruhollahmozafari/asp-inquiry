from rest_framework import serializers
from core.models import Inquiry ,Device

class BillInquirySerializer(serializers.ModelSerializer):
    device_id = serializers.IntegerField()
    class Meta:
        model = Inquiry
        # fields = '__all__'
        fields = ['device','Description','Code','Amount','PreviousDate', 'CurrentDate', 'PaymentDate', 'FullName', 'BillID', 'device_id']


    #
    # def to_representation(self, instance):
    #     ret = super(PhoneBillInquirySerializer, self).to_representation(instance)
    #
    #     data = {
    #         "Identity": {
    #             "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
    #         },
    #         "Parameters": {
    #             "MobileNumber": ret.get('Number')
    #         }
    #     }
    #     return data



class DeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Device
        # fields = '__all__'
        fields = ['Number', 'Operator','TypeLine','owner', 'name', 'last_inquiry', 'device_type', 'description']

# ---------------------------------------------------------------------------------------------------------

# OPERATORS = [
#     ('Irancell', 'Irancell'),
#     ('Rightel', 'Rightel'),
#     ('Hamrahavval', 'Hamrahavval'),
# ]
# class MobileBillInquirySerializer(serializers.ModelSerializer):
#     Operator = serializers.ChoiceField(choices=OPERATORS)
#     MobileNumber = serializers.CharField(max_length=100)

#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = []


# class RightelMobileBillInquirySerializer(serializers.ModelSerializer):
#     Amount = serializers.IntegerField(read_only=True)
#     MobileNumber = serializers.CharField(max_length=100)
#     PreviousDate = serializers.CharField(max_length=100)
#     CurrentDate = serializers.CharField(max_length=100)
#     PaymentDate = serializers.CharField(max_length=100)
#     ExtraInfo = serializers.CharField(max_length=100)
#     BillID = serializers.IntegerField()
#     PaymentID = serializers.CharField(max_length=100)

#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = []

#     def to_representation(self, instance):
#         ret = super(RightelMobileBillInquirySerializer, self).to_representation(instance)

#         data = {
#             "Identity": {
#                 "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
#             },
#             "Parameters": {
#                 "MobileNumber": ret.get('MobileNumber')
#             }
#         }
#         return data

# class MtnMobileBillInquirySerializer(serializers.ModelSerializer):
#     MobileNumber = serializers.CharField(max_length=100)
#     Amount = serializers.IntegerField(read_only=True)
#     ExtraInfo = serializers.CharField(max_length=100)
#     BillID = serializers.IntegerField()
#     PaymentID = serializers.CharField(max_length=100)

#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = []

#     def to_representation(self, instance):
#         ret = super(MtnMobileBillInquirySerializer, self).to_representation(instance)

#         data = {
#             "Identity": {
#                 "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
#             },
#             "Parameters": {
#                 "MobileNumber": ret.get('MobileNumber')
#             }
#         }
#         return data

# class IrancelMobileBillInquirySerializer(serializers.ModelSerializer):
#     MobileNumber = serializers.CharField(max_length=100)
#     TraceNumber = serializers.CharField(max_length=100, required=False)
#     CurrentDate = serializers.CharField(max_length=100, required=False)
#     Amount = serializers.IntegerField(read_only=True, required=False)
#     paymentDate = serializers.CharField(max_length=100, required=False)

#     class Meta:
#         model = Phone
#         # fields = '__all__'
#         fields = ['MobileNumber','TraceNumber','CurrentDate','Amount','paymentDate',]

#     def to_representation(self, instance):
#         ret = super(IrancelMobileBillInquirySerializer, self).to_representation(instance)

#         data = {
#             "Identity": {
#                 "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
#             },
#             "Parameters": {
#                 "MobileNumber": ret.get('MobileNumber')
#             }
#         }
#         return data



# class FixedLineBillInquirySerializer(serializers.ModelSerializer):
#     token = serializers.CharField(max_length=100)
#     FixedLineNumber = serializers.CharField(max_length=100)

#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = []

#     def to_representation(self, instance):
#         ret = super(FixedLineBillInquirySerializer, self).to_representation(instance)

#         data = {
#             "Identity": {
#                 "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
#             },
#             "Parameters": {
#                 "MobileNumber": ret.get('MobileNumber')
#             }
#         }
#         return data

# TYPELINES = [
#     ('FixedLine', 'FixedLine'),
#     ('Mobile', 'Mobile'),
# ]

# class BillInquirySerializer(serializers.ModelSerializer):
#     Operator = serializers.ChoiceField(choices=OPERATORS)
#     MobileNumber = serializers.CharField(max_length=100)
#     TypeLine = serializers.ChoiceField(choices=TYPELINES)

#     class Meta:
#         model = Phone
#         fields = '__all__'
#         # fields = []

#     def to_representation(self, instance):
#         ret = super(BillInquirySerializer, self).to_representation(instance)

#         data = {
#             "Identity": {
#                 "Token": "3074B060C52E440BABC2BAAA4FF9A8E5"
#             },
#             "Parameters": {
#                 "MobileNumber": ret.get('MobileNumber')
#             }
#         }
#         return data

# class PhoneSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Phone
#         fields = '__all__'