# Generated by Django 3.1.7 on 2021-04-08 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_models', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='raw_password',
        ),
    ]
