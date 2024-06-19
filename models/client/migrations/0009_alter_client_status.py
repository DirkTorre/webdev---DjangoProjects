# Generated by Django 4.1 on 2024-05-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0008_alter_client_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.CharField(choices=[('archived', 'Archived'), ('active', 'Active')], default='active', max_length=255),
        ),
    ]
