# Generated by Django 4.2.11 on 2024-05-19 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0004_contest_created_contest_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='상금_backup',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
