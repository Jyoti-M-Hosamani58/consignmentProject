# Generated by Django 5.0.6 on 2024-09-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consign_app', '0039_alter_addconsignment_track_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addconsignment',
            name='track_id',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='addconsignmenttemp',
            name='track_id',
            field=models.CharField(max_length=50, null=True),
        ),
    ]