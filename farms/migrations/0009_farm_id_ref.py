# Generated by Django 3.2.5 on 2022-02-07 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0008_remove_farm_quarantine_nights'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='id_ref',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
