# Generated by Django 5.0.6 on 2024-09-16 23:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0031_remove_addconsignment_commission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripsheetprem',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='AdvGiven',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='DriverName',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='LTRate',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='Ltr',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='Time',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='VehicalNo',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='commission',
        ),
    ]