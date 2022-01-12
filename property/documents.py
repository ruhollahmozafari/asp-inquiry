from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models.device_models import Inquiry, Device



@registry.register_document
class DeviceDocument(Document):
    class Index:
        name = 'device'
    # settings = {
    #     'number_of_shards': 1,
    #     'number_of_replicas': 0
    # }
    class Django:
         model = Device
         fields = [
            # 'owner',
            'name',
            'description',
            'device_type',
            'MobileNumber',
            'FixedLineNumber',
            'BarCode',
            'ElectricityBillID',
            'ParticipateCode',
            'GasBillID',
            'WaterBillID',

         ]

@registry.register_document
class InquiryDocument(Document):
    class Index:
        name = 'inquiry'
    # settings = {
    #     'number_of_shards': 1,
    #     'number_of_replicas': 0
    # }
    class Django:
         model = Inquiry
         fields = [
            #  'device',
            'id',
            'PaymentID',
            'Description',
         ]

