# Generated by Django 5.0.6 on 2024-09-06 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0018_alter_disel_liter_alter_disel_ltrate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disel',
            name='total',
            field=models.FloatField(max_length=50, null=True),
        ),
    ]