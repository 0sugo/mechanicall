# Generated by Django 4.2.7 on 2023-11-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_servicerequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
