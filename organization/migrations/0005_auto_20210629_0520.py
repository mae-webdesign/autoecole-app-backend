# Generated by Django 3.2.3 on 2021-06-29 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_auto_20210629_0512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='phone',
            field=models.CharField(max_length=14, null=True),
        ),
    ]