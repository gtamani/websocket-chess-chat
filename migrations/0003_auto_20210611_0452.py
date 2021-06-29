# Generated by Django 3.2 on 2021-06-11 07:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_auto_20210607_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(max_length=20)),
                ('player1', models.CharField(default=float("nan"), max_length=50)),
                ('player2', models.CharField(default=float("nan"), max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('turn', models.CharField(default='w', max_length=20)),
                ('fen', models.CharField(default='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 4, 52, 26, 374781), verbose_name='Inicio de sesión'),
        ),
        migrations.AlterField(
            model_name='usersconnected',
            name='connected',
            field=models.DateField(default=datetime.datetime(2021, 6, 11, 4, 52, 26, 374781), verbose_name='Fecha de Creación'),
        ),
    ]