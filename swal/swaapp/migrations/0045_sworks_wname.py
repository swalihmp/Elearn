# Generated by Django 3.2.3 on 2022-06-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0044_work_workname'),
    ]

    operations = [
        migrations.AddField(
            model_name='sworks',
            name='wname',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
