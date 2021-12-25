# Generated by Django 4.0 on 2021-12-25 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_inquiry_finalterm_amount_inquiry_finalterm_billid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='bill_type',
            field=models.CharField(blank=True, choices=[('ElectricityBill', 'ElectricityBill'), ('GasBill', 'GasBill'), ('WaterBill', 'WaterBill')], max_length=50, null=True, verbose_name='bill_type'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='Abonman',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Abonman'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='Address',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='AverageConsumption',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='AverageConsumption'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='BillPdfUrl',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='BillPdfUrl'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='ConsumptionType',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='ConsumptionType'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='CurrentCounterDigit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='CurrentCounterDigit'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='CustomerType',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='CustomerType'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='Insurance',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Insurance'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='InsuranceAmount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='InsuranceAmount'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='PowerPaytollAmount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PowerPaytollAmount'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='PreviousCounterDigit',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='PreviousCounterDigit'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='SaleYear',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='SaleYear'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='TariffType',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='TariffType'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='Tax',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tax'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='TaxAmount',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='TaxAmount'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='TotalDays',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='TotalDays'),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(blank=True, choices=[('phone', 'phone'), ('car', 'car'), ('home', 'home')], max_length=50, null=True, verbose_name='device_type'),
        ),
    ]
