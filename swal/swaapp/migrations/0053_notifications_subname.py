# Generated by Django 3.2.3 on 2022-06-30 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0052_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='subname',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
