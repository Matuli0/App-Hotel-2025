# Generated by Django 3.2 on 2025-06-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
                ('capacidad', models.IntegerField()),
                ('orientacion', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('rut', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reserva', models.DateField()),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_pasajeros.habitacion')),
                ('pasajero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_pasajeros.pasajero')),
            ],
        ),
    ]
