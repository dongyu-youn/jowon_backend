# Generated by Django 4.2.11 on 2024-11-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0003_alter_response_choice_delete_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='choice',
            field=models.IntegerField(choices=[(5, '매우잘한다'), (4, '잘한다'), (3, '보통이다'), (2, '조금 할줄안다'), (1, '경험 해본적 없다')]),
        ),
    ]