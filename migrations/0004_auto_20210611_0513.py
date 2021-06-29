# Generated by Django 3.2 on 2021-06-11 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210611_0452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 5, 13, 15, 283538), verbose_name='Inicio de sesión'),
        ),
        migrations.AlterField(
            model_name='games',
            name='fen',
            field=models.CharField(default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', max_length=120),
        ),
        migrations.AlterField(
            model_name='games',
            name='player1',
            field=models.CharField(default=float("nan"), max_length=50),
        ),
        migrations.AlterField(
            model_name='games',
            name='player2',
            field=models.CharField(default=float("nan"), max_length=50),
        ),
        migrations.AlterField(
            model_name='usersconnected',
            name='connected',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 5, 13, 15, 283538), verbose_name='Fecha de Creación'),
        ),
    ]
