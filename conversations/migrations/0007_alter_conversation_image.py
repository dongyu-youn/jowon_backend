# Generated by Django 4.2.11 on 2024-05-31 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0006_alter_conversation_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='image',
            field=models.URLField(max_length=1000, null=True),
        ),
    ]
