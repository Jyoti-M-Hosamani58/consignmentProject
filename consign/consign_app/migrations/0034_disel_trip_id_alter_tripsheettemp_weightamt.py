# Generated by Django 5.0.6 on 2024-09-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0033_remove_tripsheettemp_trip_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='disel',
            name='trip_id',
            field=models.FloatField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='tripsheettemp',
            name='weightAmt',
            field=models.FloatField(null=True),
        ),
    ]