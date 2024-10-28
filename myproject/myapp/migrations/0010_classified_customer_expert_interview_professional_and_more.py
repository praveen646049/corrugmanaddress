# Generated by Django 5.1.1 on 2024-10-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_adcustomers_classifieds_experts_interviews_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classified',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('s_no', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='AdCustomers',
        ),
        migrations.DeleteModel(
            name='Classifieds',
        ),
        migrations.DeleteModel(
            name='Experts',
        ),
        migrations.DeleteModel(
            name='Interviews',
        ),
        migrations.DeleteModel(
            name='Professionals',
        ),
    ]