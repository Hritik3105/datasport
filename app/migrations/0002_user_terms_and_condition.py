# Generated by Django 4.0.2 on 2022-02-25 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='terms_and_condition',
            field=models.BooleanField(default=0),
        ),
    ]
