# Generated by Django 2.2.4 on 2019-08-17 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_registro', '0005_auto_20190817_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participante',
            name='apellido',
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
