# Generated by Django 4.0.5 on 2022-07-12 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_modelname_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelvar',
            name='percent_value',
        ),
    ]