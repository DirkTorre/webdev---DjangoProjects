# Generated by Django 4.1 on 2024-05-09 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_todolist_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='comment',
            field=models.ManyToManyField(to='client.comment'),
        ),
    ]