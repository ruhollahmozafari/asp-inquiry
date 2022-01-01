from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Inquiry, Device

@registry.register_document
class InquiryDocument(Document):
    class Index:
        name = 'Inquiry'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Inquiry
         fields = [
             'owner',
             'device_type',
         ]


@registry.register_document
class DeviceDocument(Document):
    class Index:
        name = 'Device'
    settings = {
        'number_of_shards': 1,
        'number_of_replicas': 0
    }
    class Django:
         model = Device
         fields = [
             'device',
             'PaymentID',
         ]