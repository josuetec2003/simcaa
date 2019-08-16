# Generated by Django 2.2.3 on 2019-08-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='estado',
        ),
        migrations.AddField(
            model_name='participante',
            name='obsequio',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='participante',
            name='registrado',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Estado',
        ),
    ]