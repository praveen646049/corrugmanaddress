# Generated by Django 5.1.1 on 2024-10-08 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('region', models.CharField(max_length=100)),
                ('categories', models.CharField(max_length=100)),
                ('postal_dtdc', models.CharField(max_length=50)),
                ('person_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
                ('copies', models.PositiveIntegerField()),
                ('receiver_name', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
