# Generated by Django 4.1 on 2024-05-09 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_todolist_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.ManyToManyField(blank=True, to='client.comment'),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='comment',
            field=models.ManyToManyField(blank=True, to='client.comment'),
        ),
    ]
