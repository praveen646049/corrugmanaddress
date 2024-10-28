# Generated by Django 5.0.4 on 2024-10-20 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_address_copies'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_no', models.IntegerField()),
                ('return_address', models.CharField(max_length=255)),
                ('confirm_address', models.CharField(max_length=255)),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('verified', 'Verified'), ('not_verified', 'Not Verified'), ('rejected', 'Rejected')], default='not_verified', max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='address',
            name='copies',
            field=models.IntegerField(),
        ),
    ]
