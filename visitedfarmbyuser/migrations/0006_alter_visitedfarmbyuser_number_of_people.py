# Generated by Django 3.2.5 on 2021-11-26 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visitedfarmbyuser', '0005_visitedfarmbyuser_number_of_people'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitedfarmbyuser',
            name='number_of_people',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
