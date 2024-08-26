# Generated by Django 5.0.6 on 2024-08-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('numero_telefonico', models.CharField(max_length=15)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('num_personas', models.PositiveIntegerField()),
                ('tipo_tour', models.CharField(max_length=50)),
            ],
        ),
    ]
