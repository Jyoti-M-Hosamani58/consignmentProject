# Generated by Django 5.0.6 on 2024-09-15 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0028_alter_addconsignmenttemp_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='Date',
            field=models.DateField(null=True),
        ),
    ]
