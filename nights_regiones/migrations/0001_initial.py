# Generated by Django 3.2.5 on 2021-11-08 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('farms', '0002_alter_farm_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NightsRegiones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noroeste', models.PositiveSmallIntegerField()),
                ('veracruz', models.PositiveSmallIntegerField()),
                ('tehuacan', models.PositiveSmallIntegerField()),
                ('cordoba', models.PositiveSmallIntegerField()),
                ('farm_origen', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='farms.farm')),
            ],
            options={
                'ordering': ('farm_origen',),
            },
        ),
    ]
