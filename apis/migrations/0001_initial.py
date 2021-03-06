# Generated by Django 3.2.12 on 2022-04-10 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):


    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_id', models.CharField(max_length=64)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('company_name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('password', models.CharField(max_length=255)),
                ('contact_number', models.CharField(blank=True, max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=14)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.device')),
                ('notification', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='OperationLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(choices=[('GET RECORDS', 'Retrive account records'), ('UPDATE RECORDS', 'Update account records'), ('ADD CONTACT', 'Add Contact'), ('GET CONTACT', 'Retrive Contact'), ('UPDATE CONTACT', 'Update Contact'), ('DELETE CONTACT', 'Delete Contact'), ('GET RATE', 'Retrive Rate data'), ('UPDATE RATE', 'Update Rate data'), ('RETRIEVE ACCOUNT DETAILS', 'Retrieve account details')], max_length=24)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.device')),
            ],
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('unit', models.CharField(choices=[('GRAMME', 'G'), ('KILOGRAMME', 'KG')], default='GRAMME', max_length=24)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apis.device')),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('unit', models.CharField(choices=[('GRAMME', 'G'), ('KILOGRAMME', 'KG')], default='GRAMME', max_length=10)),
                ('currency', models.CharField(choices=[('NAIRA', 'Naira'), ('DOLLAR', 'Dollar')], default='NAIRA', max_length=24)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active_rate', models.BooleanField(default=True)),
            ],
        ),
    ]
