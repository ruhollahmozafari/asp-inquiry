from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth import get_user_model
# import factory
# from factory.django import DjangoModelFactory
User = get_user_model()
import random 

DEVICE_TYPE = [
    ('FixedLine','FixedLine'),
    ('Irancell','Irancell'),
    ('Hamrahavval','Hamrahavval'),
    ('Rightel','Rightel'),
    ('car','car'),
    ('ElectricityBill','ElectricityBill'),
    ('GasBill','GasBill'),
    ('WaterBill','WaterBill'),
    
]


class Device(models.Model):
    created_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='created_by', 
        blank=True, null=True,
    )
    owner = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        related_name='owner', 
        blank=True, null=True,
    )
    name = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    is_active = models.BooleanField(
        default=True,
        blank=True, null=True
    )
    description = models.CharField(
        max_length=250, 
        blank=True, null=True
    )
    last_inquiry = models.DateTimeField( 
        blank=True, null=True
    )
    device_type = models.CharField(
        max_length=50, 
        choices=DEVICE_TYPE, 
        blank=True, null=True
    )

    # phone
    MobileNumber = models.CharField(
        max_length=50, 
        blank=True, null=True,
    )
    FixedLineNumber = models.CharField(
        max_length=50, 
        blank=True, null=True,
    )
    
    # car
    BarCode = models.CharField(
        max_length=100, 
        blank=True, null=True,
    )

    # Home
    ElectricityBillID = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    ParticipateCode = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    GasBillID = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    WaterBillID = models.CharField(
        max_length=50, 
        blank=True, null=True
    )

    class Meta:
        ordering = ['id']
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'

    @property
    def owner_indexing(self):
        return self.owner.name

    @property
    def device_type_indexing(self):
        return self.device_type





class Inquiry(models.Model):
    device = models.ForeignKey(
        Device, 
        on_delete=models.CASCADE,
        related_name='device',
        blank=True, null=True
    )

    Code = models.CharField(
        max_length=100, 
        blank=True, null=True
    )
    Description = models.CharField(
        max_length=50, 
        blank=True, null=True
    )

    Amount = models.IntegerField(
        blank=True, null=True   
    )
    BillID = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    PaymentID = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    FullName = models.CharField(
        max_length=50,
        blank=True, null=True
    )

    is_paid = models.BooleanField(
        default=False,
        blank=True, null=True
    )
    payment_tracking_code = models.CharField(
        max_length=150,
        blank=True, null=True
    )
    # Phone
    PreviousDate = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    CurrentDate = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    PaymentDate = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    Cycle = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    TraceNumber = models.CharField(
        max_length=100, 
        blank=True, null=True,
    )
    MidTerm_Amount = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    MidTerm_BillID = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    MidTerm_PaymentID = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    FinalTerm_Amount = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    FinalTerm_BillID = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    FinalTerm_PaymentID = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    # Car
    PlateNumber = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    TotalAmount = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    Details = models.CharField(
        max_length=50,  
        blank=True, null=True
    )
    City = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    Location = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    Type = models.CharField(
        max_length=50,  
        blank=True, null=True
    )
    DateTime = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    Delivery = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    SerialNumber = models.CharField(
        max_length=50,
        blank=True, null=True
    )

    # Home
    Address = models.CharField(
        max_length=250, 
        blank=True, null=True
    )
    BillPdfUrl = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    ExtraInfo = models.TextField( 
        blank=True, null=True
    )
    ConsumptionType = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    PreviousCounterDigit = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    CurrentCounterDigit = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    Abonman = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    Tax = models.CharField(
        max_length=50,
        verbose_name='Tax', 
        blank=True, null=True
    )
    Insurance = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    TotalDays = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    PowerPaytollAmount = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    TaxAmount = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    InsuranceAmount = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    AverageConsumption = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    SaleYear = models.CharField(
        max_length=50, 
        blank=True, null=True
    )
    CustomerType = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    TariffType = models.CharField(
        max_length=50,
        blank=True, null=True
    )
    class Meta:
        ordering = ['id']
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'

    @property
    def device_indexing(self):
        if self.device is not None:
            return self.device.name

    @property
    def PaymentID_indexing(self):
        return self.PaymentID


    def __str__(self):
        return self.device.name

    def get_total_cost(self):
        if self.TotalAmount:
            return self.TotalAmount
        if self.Amount:
            return self.Amount
        if self.FinalTerm_Amount:
            return self.FinalTerm_Amount
        if self.MidTerm_Amount:
            return self.MidTerm_Amount

