# Generated by Django 3.2.5 on 2021-11-21 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0007_alter_farm_quarantine_nights'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farm',
            name='quarantine_nights',
        ),
    ]
