# Generated by Django 4.1 on 2022-11-08 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_APP', '0003_alter_reserva_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='cantidad_personas',
            field=models.IntegerField(),
        ),
    ]