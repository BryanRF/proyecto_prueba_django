# Generated by Django 5.0 on 2023-12-09 23:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Empleado",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("puesto", models.CharField(max_length=50)),
                ("fecha_nacimiento", models.DateField()),
                ("genero", models.BooleanField()),
                ("dni", models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Asistencia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fecha", models.DateField()),
                ("hora_entrada", models.TimeField()),
                ("hora_salida_almuerzo", models.TimeField()),
                ("hora_entrada_almuerzo", models.TimeField()),
                ("hora_salida", models.TimeField()),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modelos.empleado",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Horario",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("dia_semana", models.CharField(max_length=15)),
                ("hora_entrada", models.TimeField()),
                ("hora_salida_almuerzo", models.TimeField()),
                ("hora_entrada_almuerzo", models.TimeField()),
                ("hora_salida", models.TimeField()),
                (
                    "empleado",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="modelos.empleado",
                    ),
                ),
            ],
        ),
    ]
