# Generated by Django 4.1 on 2023-02-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.DecimalField(decimal_places=1, max_digits=9),
        ),
    ]
