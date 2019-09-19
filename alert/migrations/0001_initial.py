# Generated by Django 2.2.5 on 2019-09-18 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Сирена', 'Сирена'), ('Громкоговоритель', 'Громкоговоритель')], max_length=100, verbose_name='Тип устройства')),
                ('address', models.CharField(max_length=100, unique=True, verbose_name='Адресс устройства')),
                ('Latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Широта')),
                ('Longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True, verbose_name='Долгота')),
                ('radius_soundcover', models.IntegerField(verbose_name='Радиус зоны звукопокрытия')),
                ('activity', models.BooleanField(default=False, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Устройство',
                'verbose_name_plural': 'Устройства',
            },
        ),
    ]