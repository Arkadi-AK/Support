# Generated by Django 4.0 on 2022-01-05 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='support',
            field=models.BooleanField(default=False),
        ),
    ]
