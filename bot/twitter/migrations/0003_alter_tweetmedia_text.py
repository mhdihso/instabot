# Generated by Django 3.2.1 on 2021-05-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_account_is_managerdb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetmedia',
            name='text',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]