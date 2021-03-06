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
            name='NightsVeracruz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iguazu', models.PositiveSmallIntegerField()),
                ('mata_espino', models.PositiveSmallIntegerField()),
                ('gertrudis', models.PositiveSmallIntegerField()),
                ('capulines_1', models.PositiveSmallIntegerField()),
                ('angelito', models.PositiveSmallIntegerField()),
                ('capulines_2', models.PositiveSmallIntegerField()),
                ('palomas', models.PositiveSmallIntegerField()),
                ('milagro', models.PositiveSmallIntegerField()),
                ('capulines_rentado', models.PositiveSmallIntegerField()),
                ('cuarentena', models.PositiveSmallIntegerField()),
                ('gloria', models.PositiveSmallIntegerField()),
                ('cruz', models.PositiveSmallIntegerField()),
                ('gregorio', models.PositiveSmallIntegerField()),
                ('copital', models.PositiveSmallIntegerField()),
                ('cuarentena_lupita', models.PositiveSmallIntegerField()),
                ('oficina_angelito', models.PositiveSmallIntegerField()),
                ('almacen_general', models.PositiveSmallIntegerField()),
                ('planta_alimentos', models.PositiveSmallIntegerField()),
                ('venta_deposito', models.PositiveSmallIntegerField()),
                ('farm_origen', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='farms.farm')),
            ],
        ),
    ]
