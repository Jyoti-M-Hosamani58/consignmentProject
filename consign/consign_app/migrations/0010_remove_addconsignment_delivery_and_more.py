# Generated by Django 5.0.6 on 2024-08-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0009_rename_godown_addconsignment_delivery_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addconsignment',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='addconsignmenttemp',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='tripsheetprem',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='tripsheettemp',
            name='commission',
        ),
        migrations.AddField(
            model_name='addconsignment',
            name='commission',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='addconsignmenttemp',
            name='commission',
            field=models.FloatField(null=True),
        ),
    ]
