# Generated by Django 3.2.1 on 2021-05-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0009_searchintraction'),
    ]

    operations = [
        migrations.CreateModel(
            name='searchdirectmassage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('args', models.CharField(max_length=100)),
                ('text_direct', models.CharField(max_length=500)),
            ],
        ),
    ]