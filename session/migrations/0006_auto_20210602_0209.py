# Generated by Django 3.2.3 on 2021-06-02 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0005_auto_20210602_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='debrief',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='location',
            field=models.CharField(blank=True, max_length=75, null=True),
        ),
    ]