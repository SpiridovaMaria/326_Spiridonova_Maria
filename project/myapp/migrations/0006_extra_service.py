# Generated by Django 4.2.6 on 2023-11-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_passangers_and_flights_id_flight_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Extra_service',
            fields=[
                ('id', models.IntegerField(help_text='Введите id', primary_key=True, serialize=False, verbose_name='id')),
                ('service_name', models.CharField(help_text='Введите название услуги', max_length=50, verbose_name='Название услуги')),
            ],
            options={
                'db_table': 'Extra_service',
            },
        ),
    ]
