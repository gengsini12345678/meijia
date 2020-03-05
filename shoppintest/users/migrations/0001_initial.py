# Generated by Django 2.0.3 on 2019-12-14 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('header', models.ImageField(default='static/images/headers/default.jpg', upload_to='static/images/headers/')),
                ('nickname', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('age', models.IntegerField(default=0)),
                ('gender', models.CharField(max_length=5)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
