# Generated by Django 3.2.3 on 2021-06-29 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0003_alter_session_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='session',
            old_name='start_date',
            new_name='date',
        ),
    ]
