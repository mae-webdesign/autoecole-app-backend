# Generated by Django 3.2.3 on 2021-06-29 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_organization_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='city',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='country',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='postalcode',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='street',
        ),
        migrations.AddField(
            model_name='organization',
            name='address',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(default='', max_length=14),
        ),
    ]