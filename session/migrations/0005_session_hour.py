# Generated by Django 3.2.3 on 2021-06-29 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0004_rename_start_date_session_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='hour',
            field=models.TimeField(null=True),
        ),
    ]
