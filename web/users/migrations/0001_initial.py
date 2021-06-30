# Generated by Django 3.2.3 on 2021-06-29 07:30

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('firstname', models.CharField(default='', max_length=50)),
                ('lastname', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=14)),
                ('street', models.CharField(default='', max_length=75)),
                ('city', models.CharField(default='', max_length=75)),
                ('postalcode', models.CharField(default='', max_length=7)),
                ('country', models.CharField(default='', max_length=30)),
                ('birthday', models.DateField(null=True)),
                ('bio', models.CharField(default='', max_length=150)),
                ('is_student', models.BooleanField(default=False)),
                ('is_instructor', models.BooleanField(default=False)),
                ('is_org_admin', models.BooleanField(default=False)),
                ('organization_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]