# Generated by Django 4.2.7 on 2023-11-27 12:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_mechanic_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='tow',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
