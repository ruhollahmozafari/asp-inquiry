from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


# class Inquiry(models.Model):
#
#     class Meta:
#         abstract = True
#         ordering = ['id']
#         verbose_name = 'Inquiry'
#         verbose_name_plural = 'Inquiries'

"""

class RightelMobileInquiry(models.Model):
    previous_date = models.CharField(max_length=250, verbose_name='previous_date')
    extra_info = models.IntegerField(verbose_name='extra_info')
    bill_ID = models.CharField(max_length=250, verbose_name='bill_ID')
    payment_ID = models.CharField(max_length=250, verbose_name='payment_ID')

    class Meta:
        ordering = ['id']
        verbose_name = 'RightelMobileInquiry'
        verbose_name_plural = 'RightelMobileInquiry'


class PhoneInquiry(models.Model):
    cycle = models.CharField(max_length=250, verbose_name='cycle')
    mount = models.IntegerField(verbose_name='mount')
    bill_ID = models.CharField(max_length=250, verbose_name='bill_ID')
    payment_ID = models.CharField(max_length=250, verbose_name='payment_ID')

    class Meta:
        ordering = ['id']
        verbose_name = 'PhoneInquiry'
        verbose_name_plural = 'PhoneInquiries'


class DrivingOffensesInquiry(models.Model):
    plate_number = models.CharField(max_length=250, verbose_name='plate_number')
    total_amount = models.IntegerField(verbose_name='total_amount')
    details = models.CharField(max_length=250, verbose_name='plate_number',null=True, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'DrivingOffensesInquiry'
        verbose_name_plural = 'DrivingOffensesInquiries'


class Device(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='staff_college')
    discount = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)],verbose_name='discount')
    active = models.BooleanField(verbose_name='active')

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'


# ZONE_LETTERS = [
#     ('b','ب'),
#     ('g','ج'),
#     #...
# ]
# class CarCode(models.Model):
#     zone_letter = models.CharField(max_length=50, choices=ZONE_LETTERS,verbose_name='zone_letter')
#     zone_code = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(2)],verbose_name='discount')
#     main_code = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(5)], verbose_name='main_code')
#
#     class Meta:
#         ordering = ['id']
#         verbose_name = 'CarCode'
#         verbose_name_plural = 'CarCodes'
#
#     def __str__(self):
#         return str(self.main_code)[:1] + str(self.zone_letter) + str(self.main_code)[2:] + str(self.zone_code)

class Car(Device):
    # code = models.ForeignKey(CarCode, on_delete=models.CASCADE,related_name='staff_college')
    bar_code = models.CharField(max_length=50, verbose_name='bar_code')

    class Meta:
        ordering = ['id']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.code


class BasePhone(Device):
    is_active = models.BooleanField(verbose_name='active')

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'BasePhone'
        verbose_name_plural = 'BasePhones'

    # @property
    # def active(self):
    #     if timezone.now() > self.valid_to:
    #         return False
    #     return True


class Phone(BasePhone):
    fixed_line_number = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)], verbose_name='fixed_line_number')
    inquirys = models.ForeignKey(PhoneInquiry, on_delete=models.CASCADE, related_name='mobile_inquirys')

    class Meta:
        ordering = ['id']
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self):
        return


OPERATORS = [
    ('raghtel','raghtel'),
    ('irancel','irancel'),
    #...
]
class Mobile(BasePhone):
    phone_number = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)], verbose_name='phone_number')
    # inquirys = models.ForeignKey(Inquiry, on_delete=models.CASCADE,related_name='mobile_inquirys')
    operator = models.CharField(max_length=50, choices=OPERATORS,verbose_name='zone_letter')

    class Meta:
        ordering = ['id']
        verbose_name = 'Mobile'
        verbose_name_plural = 'Mobiles'

    def __str__(self):
        return

class MtnMobileBillInquiry(Mobile):
    amount = models.CharField(max_length=50, verbose_name='zone_letter', blank=True, null=True),
    billID = models.CharField(max_length=50, verbose_name='zone_letter', blank=True, null=True),
    extraInfo = models.CharField(max_length=50, verbose_name='zone_letter', blank=True, null=True),
    paymentID = models.CharField(max_length=50, verbose_name='zone_letter', blank=True, null=True),

    class Meta:
        ordering = ['id']
        verbose_name = 'MtnMobileBillInquiry'
        verbose_name_plural = 'MtnMobileBillInquiry'

    def __str__(self):
        return

"""

# ------------------------------------------------------------------------------------------------------------------
# MtnMobileBillInquiry
# class IrancelMobileBillInquiry(models.Model):
#     MobileNumber = models.CharField(max_length=100, verbose_name='MobileNumber'),
#     Description = models.CharField(max_length=250, verbose_name='Description'),
#     Code = models.CharField(max_length=50, verbose_name='Code'),
#     Amount = models.CharField(max_length=50, verbose_name='Amount', blank=True, null=True),
#     BillID = models.CharField(max_length=50, verbose_name='BillID', blank=True, null=True),
#     ExtraInfo = models.CharField(max_length=50, verbose_name='ExtraInfo', blank=True, null=True),
#     PaymentID = models.CharField(max_length=50, verbose_name='PaymentID', blank=True, null=True),
#
#
#     class Meta:
#         ordering = ['id']
#         verbose_name = 'IrancelMobileBillInquiry'
#         verbose_name_plural = 'IrancelMobileBillInquiries'
#
#     def __str__(self):
#         return self.MobileNumber

class Phone(models.Model):
    Number = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)], verbose_name='FixedLineNumber', blank=True, null=True)
    Amount = models.IntegerField(verbose_name='Amount', blank=True, null=True),
    PreviousDate = models.CharField(max_length=50,verbose_name='PreviousDate', blank=True, null=True)
    CurrentDate = models.CharField(max_length=50,verbose_name='CurrentDate', blank=True, null=True)
    PaymentDate = models.CharField(max_length=50,verbose_name='PaymentDate', blank=True, null=True)
    FullName = models.CharField(max_length=50,verbose_name='FullName', blank=True, null=True)
    BillID = models.CharField(max_length=50,verbose_name='BillID', blank=True, null=True)
    PaymentID = models.CharField(max_length=50,verbose_name='PaymentID', blank=True, null=True)
    Cycle = models.CharField(max_length=50, verbose_name='zone_letter', blank=True, null=True)
    Operator = models.CharField(max_length=50, verbose_name='Operator', blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self):
        return

