# Generated by Django 3.2.3 on 2022-06-26 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0028_sworks'),
    ]

    operations = [
        migrations.AddField(
            model_name='sworks',
            name='wsname',
            field=models.CharField(default=0, max_length=20),
        ),
    ]