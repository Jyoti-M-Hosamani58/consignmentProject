# Generated by Django 5.0.6 on 2024-09-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0022_alter_disel_vehicalno'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripsheetprem',
            name='weightAmt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripsheettemp',
            name='weightAmt',
            field=models.IntegerField(null=True),
        ),
    ]
