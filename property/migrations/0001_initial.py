# Generated by Django 4.0 on 2022-01-01 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('last_inquiry', models.DateTimeField(blank=True, null=True)),
                ('device_type', models.CharField(blank=True, choices=[('FixedLine', 'FixedLine'), ('Irancell', 'Irancell'), ('Hamrahavval', 'Hamrahavval'), ('Rightel', 'Rightel'), ('car', 'car'), ('ElectricityBill', 'ElectricityBill'), ('GasBill', 'GasBill'), ('WaterBill', 'WaterBill')], max_length=50, null=True)),
                ('MobileNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('FixedLineNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('BarCode', models.CharField(blank=True, max_length=100, null=True)),
                ('ElectricityBillID', models.CharField(blank=True, max_length=50, null=True)),
                ('ParticipateCode', models.CharField(blank=True, max_length=50, null=True)),
                ('GasBillID', models.CharField(blank=True, max_length=50, null=True)),
                ('WaterBillID', models.CharField(blank=True, max_length=50, null=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='auth.user')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='auth.user')),
            ],
            options={
                'verbose_name': 'Device',
                'verbose_name_plural': 'Devices',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Code', models.CharField(blank=True, max_length=100, null=True)),
                ('Description', models.CharField(blank=True, max_length=50, null=True)),
                ('Amount', models.IntegerField(blank=True, null=True)),
                ('BillID', models.CharField(blank=True, max_length=50, null=True)),
                ('PaymentID', models.CharField(blank=True, max_length=50, null=True)),
                ('FullName', models.CharField(blank=True, max_length=50, null=True)),
                ('PreviousDate', models.CharField(blank=True, max_length=50, null=True)),
                ('CurrentDate', models.CharField(blank=True, max_length=50, null=True)),
                ('PaymentDate', models.CharField(blank=True, max_length=50, null=True)),
                ('Cycle', models.CharField(blank=True, max_length=50, null=True)),
                ('TraceNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('MidTerm_Amount', models.CharField(blank=True, max_length=50, null=True)),
                ('MidTerm_BillID', models.CharField(blank=True, max_length=50, null=True)),
                ('MidTerm_PaymentID', models.CharField(blank=True, max_length=50, null=True)),
                ('FinalTerm_Amount', models.CharField(blank=True, max_length=50, null=True)),
                ('FinalTerm_BillID', models.CharField(blank=True, max_length=50, null=True)),
                ('FinalTerm_PaymentID', models.CharField(blank=True, max_length=50, null=True)),
                ('PlateNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('TotalAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('Details', models.CharField(blank=True, max_length=50, null=True)),
                ('City', models.CharField(blank=True, max_length=50, null=True)),
                ('Location', models.CharField(blank=True, max_length=50, null=True)),
                ('Type', models.CharField(blank=True, max_length=50, null=True)),
                ('DateTime', models.CharField(blank=True, max_length=50, null=True)),
                ('Delivery', models.CharField(blank=True, max_length=50, null=True)),
                ('SerialNumber', models.CharField(blank=True, max_length=50, null=True)),
                ('Address', models.CharField(blank=True, max_length=250, null=True)),
                ('BillPdfUrl', models.CharField(blank=True, max_length=50, null=True)),
                ('ExtraInfo', models.TextField(blank=True, null=True)),
                ('ConsumptionType', models.CharField(blank=True, max_length=50, null=True)),
                ('PreviousCounterDigit', models.CharField(blank=True, max_length=50, null=True)),
                ('CurrentCounterDigit', models.CharField(blank=True, max_length=50, null=True)),
                ('Abonman', models.CharField(blank=True, max_length=50, null=True)),
                ('Tax', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tax')),
                ('Insurance', models.CharField(blank=True, max_length=50, null=True)),
                ('TotalDays', models.CharField(blank=True, max_length=50, null=True)),
                ('PowerPaytollAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('TaxAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('InsuranceAmount', models.CharField(blank=True, max_length=50, null=True)),
                ('AverageConsumption', models.CharField(blank=True, max_length=50, null=True)),
                ('SaleYear', models.CharField(blank=True, max_length=50, null=True)),
                ('CustomerType', models.CharField(blank=True, max_length=50, null=True)),
                ('TariffType', models.CharField(blank=True, max_length=50, null=True)),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='device', to='property.device')),
            ],
            options={
                'verbose_name': 'Inquiry',
                'verbose_name_plural': 'Inquiries',
                'ordering': ['id'],
            },
        ),
    ]