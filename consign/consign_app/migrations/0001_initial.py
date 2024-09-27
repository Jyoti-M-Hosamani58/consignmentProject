# Generated by Django 5.0.6 on 2024-08-26 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=50, null=True)),
                ('track_number', models.CharField(max_length=50, unique=True)),
                ('debit', models.CharField(max_length=50, null=True)),
                ('credit', models.CharField(max_length=50, null=True)),
                ('Balance', models.CharField(max_length=50, null=True)),
                ('sender_name', models.CharField(max_length=255)),
                ('TrType', models.CharField(max_length=50, null=True)),
                ('particulars', models.CharField(max_length=50, null=True)),
                ('headname', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddConsignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=50, null=True)),
                ('sender_name', models.CharField(max_length=50, null=True)),
                ('sender_mobile', models.CharField(max_length=50, null=True)),
                ('sender_email', models.CharField(max_length=50, null=True)),
                ('sender_address', models.CharField(max_length=50, null=True)),
                ('sender_company', models.CharField(max_length=50, null=True)),
                ('sender_GST', models.CharField(max_length=50, null=True)),
                ('receiver_name', models.CharField(max_length=50, null=True)),
                ('receiver_mobile', models.CharField(max_length=50, null=True)),
                ('receiver_email', models.CharField(max_length=50, null=True)),
                ('receiver_address', models.CharField(max_length=50, null=True)),
                ('receiver_company', models.CharField(max_length=50, null=True)),
                ('receiver_GST', models.CharField(max_length=50, null=True)),
                ('total_cost', models.IntegerField(null=True)),
                ('date', models.CharField(max_length=30, null=True)),
                ('pay_status', models.CharField(max_length=30, null=True)),
                ('route_from', models.CharField(max_length=30, null=True)),
                ('route_to', models.CharField(max_length=30, null=True)),
                ('desc_product', models.CharField(max_length=150, null=True)),
                ('pieces', models.IntegerField(null=True)),
                ('prod_invoice', models.CharField(max_length=50, null=True)),
                ('prod_price', models.CharField(max_length=50, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('freight', models.IntegerField(null=True)),
                ('hamali', models.IntegerField(null=True)),
                ('door_charge', models.IntegerField(null=True)),
                ('st_charge', models.IntegerField(null=True)),
                ('Consignment_id', models.IntegerField(null=True)),
                ('branch', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('balance', models.IntegerField(null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('copy_type', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddConsignmentTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=50, null=True)),
                ('sender_name', models.CharField(max_length=50, null=True)),
                ('sender_mobile', models.CharField(max_length=50, null=True)),
                ('sender_email', models.CharField(max_length=50, null=True)),
                ('sender_address', models.CharField(max_length=50, null=True)),
                ('sender_company', models.CharField(max_length=50, null=True)),
                ('sender_GST', models.CharField(max_length=50, null=True)),
                ('receiver_name', models.CharField(max_length=50, null=True)),
                ('receiver_mobile', models.CharField(max_length=50, null=True)),
                ('receiver_email', models.CharField(max_length=50, null=True)),
                ('receiver_address', models.CharField(max_length=50, null=True)),
                ('receiver_company', models.CharField(max_length=50, null=True)),
                ('receiver_GST', models.CharField(max_length=50, null=True)),
                ('total_cost', models.IntegerField(null=True)),
                ('date', models.CharField(max_length=30, null=True)),
                ('pay_status', models.CharField(max_length=30, null=True)),
                ('route_from', models.CharField(max_length=30, null=True)),
                ('route_to', models.CharField(max_length=30, null=True)),
                ('desc_product', models.CharField(max_length=150, null=True)),
                ('pieces', models.IntegerField(null=True)),
                ('prod_invoice', models.CharField(max_length=50, null=True)),
                ('prod_price', models.CharField(max_length=50, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('freight', models.IntegerField(null=True)),
                ('hamali', models.IntegerField(null=True)),
                ('door_charge', models.IntegerField(null=True)),
                ('st_charge', models.IntegerField(null=True)),
                ('Consignment_id', models.IntegerField(null=True)),
                ('branch', models.CharField(max_length=150, null=True)),
                ('name', models.CharField(max_length=150, null=True)),
                ('balance', models.IntegerField(null=True)),
                ('time', models.CharField(max_length=50, null=True)),
                ('copy_type', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AddTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_id', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=30, null=True)),
                ('description', models.CharField(max_length=30, null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headname', models.CharField(max_length=150, null=True)),
                ('companyname', models.CharField(max_length=50, null=True)),
                ('phonenumber', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('gst', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('image', models.CharField(max_length=50, null=True)),
                ('password', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consignee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver_name', models.CharField(max_length=50, null=True)),
                ('receiver_mobile', models.CharField(max_length=50, null=True)),
                ('receiver_email', models.CharField(max_length=50, null=True)),
                ('receiver_address', models.CharField(max_length=50, null=True)),
                ('receiver_company', models.CharField(max_length=50, null=True)),
                ('receiver_GST', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Consignor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50, null=True)),
                ('sender_mobile', models.CharField(max_length=50, null=True)),
                ('sender_email', models.CharField(max_length=50, null=True)),
                ('sender_address', models.CharField(max_length=50, null=True)),
                ('sender_company', models.CharField(max_length=50, null=True)),
                ('sender_GST', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=50, null=True)),
                ('address', models.CharField(max_length=50, null=True)),
                ('vehicle_number', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=150, null=True)),
                ('Reason', models.CharField(max_length=150, null=True)),
                ('Amount', models.CharField(max_length=150, null=True)),
                ('branch', models.CharField(max_length=150, null=True)),
                ('username', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, null=True)),
                ('feedback', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(max_length=150, null=True)),
                ('longitude', models.CharField(max_length=150, null=True)),
                ('city', models.CharField(max_length=150, null=True)),
                ('created_at', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50, null=True)),
                ('utype', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffname', models.CharField(max_length=150, null=True)),
                ('staffPhone', models.CharField(max_length=150, null=True)),
                ('staffaddress', models.CharField(max_length=150, null=True)),
                ('aadhar', models.CharField(max_length=150, null=True)),
                ('staffid', models.CharField(max_length=150, null=True)),
                ('Branch', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripSheetPrem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DriverName', models.CharField(max_length=150, null=True)),
                ('VehicalNo', models.CharField(max_length=150, null=True)),
                ('AdvGiven', models.CharField(max_length=150, null=True)),
                ('Time', models.TimeField(null=True)),
                ('Date', models.DateField(null=True)),
                ('LTRate', models.FloatField(null=True)),
                ('Ltr', models.FloatField(null=True)),
                ('LRno', models.IntegerField(null=True)),
                ('qty', models.FloatField(null=True)),
                ('desc', models.CharField(max_length=150, null=True)),
                ('dest', models.CharField(max_length=150, null=True)),
                ('consignee', models.CharField(max_length=150, null=True)),
                ('commission', models.FloatField(null=True)),
                ('username', models.CharField(max_length=150, null=True)),
                ('pay_status', models.CharField(max_length=150, null=True)),
                ('branch', models.CharField(max_length=150, null=True)),
                ('total_cost', models.FloatField(null=True)),
                ('freight', models.FloatField(null=True)),
                ('hamali', models.FloatField(null=True)),
                ('st_charge', models.FloatField(null=True)),
                ('door_charge', models.FloatField(null=True)),
                ('trip_id', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TripSheetTemp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DriverName', models.CharField(max_length=150, null=True)),
                ('VehicalNo', models.CharField(max_length=150, null=True)),
                ('AdvGiven', models.CharField(max_length=150, null=True)),
                ('Time', models.TimeField(null=True)),
                ('Date', models.DateField(null=True)),
                ('LTRate', models.FloatField(null=True)),
                ('Ltr', models.FloatField(null=True)),
                ('LRno', models.IntegerField(null=True)),
                ('qty', models.FloatField(null=True)),
                ('desc', models.CharField(max_length=150, null=True)),
                ('dest', models.CharField(max_length=150, null=True)),
                ('consignee', models.CharField(max_length=150, null=True)),
                ('commission', models.FloatField(null=True)),
                ('username', models.CharField(max_length=150, null=True)),
                ('pay_status', models.CharField(max_length=150, null=True)),
                ('branch', models.CharField(max_length=150, null=True)),
                ('total_cost', models.FloatField(null=True)),
                ('freight', models.FloatField(null=True)),
                ('hamali', models.FloatField(null=True)),
                ('st_charge', models.FloatField(null=True)),
                ('door_charge', models.FloatField(null=True)),
                ('trip_id', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
