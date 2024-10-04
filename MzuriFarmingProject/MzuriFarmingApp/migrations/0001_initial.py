# Generated by Django 5.1.1 on 2024-10-04 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CropName', models.CharField(max_length=100)),
                ('ScientificName', models.CharField(max_length=100)),
                ('AverageYield', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Farmers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=100)),
                ('PhoneNumber', models.CharField(max_length=15)),
                ('Location', models.CharField(max_length=255)),
                ('FarmSize', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='SoilConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=255)),
                ('pH', models.DecimalField(decimal_places=2, max_digits=4)),
                ('OrganicMatter', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Nitrogen', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Phosphorus', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Potassium', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=64)),
                ('Email', models.EmailField(max_length=100, unique=True)),
                ('Role', models.CharField(choices=[('Farmer', 'Farmer'), ('Agronomist', 'Agronomist'), ('Researcher', 'Researcher'), ('Admin', 'Admin')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location', models.CharField(max_length=255)),
                ('Date', models.DateField()),
                ('Temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Rainfall', models.DecimalField(decimal_places=2, max_digits=5)),
                ('WeatherCondition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CropYield',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Year', models.IntegerField()),
                ('Yield', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Crop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.crops')),
                ('Farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.farmers')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Plan', models.CharField(choices=[('Basic', 'Basic'), ('Standard', 'Standard'), ('Professional', 'Professional')], max_length=15)),
                ('StartDate', models.DateField()),
                ('EndDate', models.DateField()),
                ('Status', models.CharField(max_length=15)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.users')),
            ],
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ReportType', models.CharField(max_length=15)),
                ('GeneratedAt', models.DateTimeField(auto_now_add=True)),
                ('ReportData', models.TextField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.users')),
            ],
        ),
        migrations.AddField(
            model_name='farmers',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.users'),
        ),
        migrations.CreateModel(
            name='ConsultingRequests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RequestDate', models.DateTimeField(auto_now_add=True)),
                ('Status', models.CharField(max_length=15)),
                ('Description', models.TextField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MzuriFarmingApp.users')),
            ],
        ),
    ]
