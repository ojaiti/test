# Generated by Django 3.2.5 on 2021-11-18 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0006_alter_farm_quarantine_nights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='quarantine_nights',
            field=models.JSONField(default=dict),
        ),
    ]