# Generated by Django 5.1.7 on 2025-03-23 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0002_contactform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.CharField(max_length=100),
        ),
    ]
