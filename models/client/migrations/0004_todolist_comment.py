# Generated by Django 4.1 on 2024-05-09 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0003_client_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='comment',
            field=models.ManyToManyField(to='client.comment'),
        ),
    ]
