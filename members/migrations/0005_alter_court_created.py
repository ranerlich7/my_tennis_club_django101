# Generated by Django 5.1.1 on 2024-09-13 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_court_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='created',
            field=models.DateTimeField(null=True),
        ),
    ]
