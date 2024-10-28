# Generated by Django 5.1.1 on 2024-10-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_classified_customer_expert_interview_professional_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='copies',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addressrecord',
            name='s_no',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='classified',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='expert',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='interview',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='end_month',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='start_month',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='total_copies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='year',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='professional',
            name='s_no',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]