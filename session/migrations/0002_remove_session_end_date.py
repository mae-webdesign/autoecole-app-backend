# Generated by Django 3.2.3 on 2021-06-29 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='end_date',
        ),
    ]
