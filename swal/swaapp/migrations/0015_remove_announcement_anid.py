# Generated by Django 3.2.3 on 2022-06-14 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0014_auto_20220531_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='anid',
        ),
    ]
