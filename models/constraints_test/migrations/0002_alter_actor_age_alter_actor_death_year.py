# Generated by Django 4.1 on 2024-05-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constraints_test', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='age',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='actor',
            name='death_year',
            field=models.IntegerField(blank=True),
        ),
    ]