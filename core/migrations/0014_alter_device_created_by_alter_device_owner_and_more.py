# Generated by Django 4.0 on 2021-12-29 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0013_alter_device_created_by_alter_device_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='device',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='auth.user'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='TraceNumber',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='TraceNumber'),
        ),
    ]
