# Generated by Django 4.1 on 2024-05-09 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('constraints_test', '0004_alter_actor_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='death_year',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
