# Generated by Django 5.0.6 on 2024-09-16 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0032_remove_tripsheetprem_commission_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='trip_id',
        ),
    ]
