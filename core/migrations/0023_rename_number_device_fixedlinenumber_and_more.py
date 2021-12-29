# Generated by Django 4.0 on 2021-12-29 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_device_gasbillid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='device',
            old_name='Number',
            new_name='FixedLineNumber',
        ),
        migrations.AddField(
            model_name='device',
            name='MobileNumber',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
