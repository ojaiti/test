# Generated by Django 3.2.5 on 2021-11-09 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nights_cordoba', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_2000',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_500',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_km_11_s3',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_s2',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_s3',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_s4',
            field=models.PositiveSmallIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='nightscordoba',
            name='tarara_s5',
            field=models.PositiveSmallIntegerField(default=2),
        ),
    ]
