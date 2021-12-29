# Generated by Django 4.0 on 2021-12-29 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_inquiry_extrainfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='Address',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='ExtraInfo',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='ExtraInfo'),
        ),
    ]
