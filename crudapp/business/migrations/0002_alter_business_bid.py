# Generated by Django 4.2.6 on 2023-10-06 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='bid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
