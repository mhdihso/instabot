# Generated by Django 3.2.1 on 2021-05-26 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_managerdb',
            field=models.BooleanField(default=False),
        ),
    ]
