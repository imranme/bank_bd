# Generated by Django 5.0 on 2024-11-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='city',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='postel_code',
        ),
        migrations.RemoveField(
            model_name='useraddress',
            name='street_address',
        ),
        migrations.RemoveField(
            model_name='userbankaccount',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='userbankaccount',
            name='gender',
        ),
        migrations.AlterField(
            model_name='userbankaccount',
            name='account_no',
            field=models.IntegerField(unique=True),
        ),
    ]
