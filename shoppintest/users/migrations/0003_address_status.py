# Generated by Django 2.0.3 on 2019-12-21 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
