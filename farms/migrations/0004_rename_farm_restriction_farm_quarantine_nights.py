# Generated by Django 3.2.5 on 2021-11-16 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0003_farm_farm_restriction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='farm',
            old_name='farm_restriction',
            new_name='quarantine_nights',
        ),
    ]
