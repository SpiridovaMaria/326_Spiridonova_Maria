# Generated by Django 4.2.6 on 2023-10-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_passenger_with_baggage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='passangers_and_flights',
            name='baggage_weight',
            field=models.IntegerField(blank=True, help_text='Введите вес багажа', null=True, verbose_name='вес багажа'),
        ),
    ]
