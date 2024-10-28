# Generated by Django 5.1.1 on 2024-10-28 11:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_addresshistory_addressrecordhistory_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='categories',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, size=None),
        ),
    ]