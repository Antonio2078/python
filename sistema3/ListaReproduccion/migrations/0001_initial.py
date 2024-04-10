# Generated by Django 5.0.3 on 2024-04-03 19:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nick', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('duracion', models.TimeField()),
                ('usuario_nick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ListaReproduccion.usuario')),
            ],
        ),
    ]