# Generated by Django 5.1.1 on 2024-10-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_monthlycopiessummary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlycopiessummary',
            options={'ordering': ['year', 'month']},
        ),
        migrations.AddField(
            model_name='monthlycopiessummary',
            name='year',
            field=models.PositiveIntegerField(default=2024),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='month',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='monthlycopiessummary',
            name='total_copies',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='monthlycopiessummary',
            unique_together={('year', 'month')},
        ),
    ]
