# Generated by Django 4.1.2 on 2022-10-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=6)),
                ('modelo', models.CharField(max_length=20, null=True)),
                ('descripcion', models.TextField(max_length=100)),
                ('disponible', models.BooleanField(default=True)),
                ('valor', models.IntegerField()),
            ],
        ),
    ]