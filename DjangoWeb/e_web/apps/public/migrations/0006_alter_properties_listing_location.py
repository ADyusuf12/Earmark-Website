# Generated by Django 5.0.7 on 2024-08-17 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_alter_properties_listing_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='properties_listing',
            name='location',
            field=models.CharField(choices=[('kano', 'Kano'), ('abuja', 'Abuja')], max_length=50),
        ),
    ]
