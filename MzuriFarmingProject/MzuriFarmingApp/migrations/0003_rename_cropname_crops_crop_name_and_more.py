# Generated by Django 5.1.1 on 2024-10-17 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MzuriFarmingApp', '0002_rename_crop_name_crops_cropname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crops',
            old_name='cropName',
            new_name='crop_name',
        ),
        migrations.RenameField(
            model_name='crops',
            old_name='scientificName',
            new_name='scientific_name',
        ),
    ]
