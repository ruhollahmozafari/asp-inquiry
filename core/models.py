from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()

class Device(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name='staff_college')
    discount = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)],verbose_name='discount')
    active = models.BooleanField(verbose_name='active')

    class Meta:
        abstract = True
        ordering = ['id']
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'


ZONE_LETTERS = [
    ('b','ب'),
    ('g','ج'),
    #...
]
class CarCode(models.Model):
    zone_letter = models.CharField(max_length=50, choices=ZONE_LETTERS,verbose_name='code')
    zone_code = models.IntegerField(validators=[MinValueValidator(2), MaxValueValidator(2)],verbose_name='discount')
    main_code = models.IntegerField(validators=[MinValueValidator(5), MaxValueValidator(5)], verbose_name='main_code')

    class Meta:
        ordering = ['id']
        verbose_name = 'CarCode'
        verbose_name_plural = 'CarCodes'

    def __str__(self):
        return str(self.main_code)[:1] + str(self.zone_letter) + str(self.main_code)[2:] + str(self.zone_code)

class Car(Device):
    code = models.ForeignKey(CarCode, on_delete=models.CASCADE,related_name='staff_college')

    class Meta:
        ordering = ['id']
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.code


class BasePhone(Device):
    phone_number = models.IntegerField(validators=[MinValueValidator(11), MaxValueValidator(11)],verbose_name='phone_number')
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

    class Meta:
        ordering = ['id']
        verbose_name = 'Phone'
        verbose_name_plural = 'Phones'

    def __str__(self):
        return



class Mobile(BasePhone):

    class Meta:
        ordering = ['id']
        verbose_name = 'Mobile'
        verbose_name_plural = 'Mobiles'

    def __str__(self):
        return