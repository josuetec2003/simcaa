# Generated by Django 2.2.4 on 2019-08-17 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0006_auto_20190817_0110'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participante',
            name='apellido',
        ),
    ]