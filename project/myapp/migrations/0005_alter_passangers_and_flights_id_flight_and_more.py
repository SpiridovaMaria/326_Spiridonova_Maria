# Generated by Django 4.2.6 on 2023-11-12 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_passangers_and_flights_baggage_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passangers_and_flights',
            name='id_flight',
            field=models.ForeignKey(default='PD 6543', help_text='Выберите рейс', on_delete=django.db.models.deletion.CASCADE, to='myapp.flights', verbose_name='flight'),
        ),
        migrations.AlterField(
            model_name='passangers_and_flights',
            name='with_baggage',
            field=models.BooleanField(blank=True, default=True, help_text='Пассажир летит с багажом?', null=True, verbose_name='багаж'),
        ),
    ]
