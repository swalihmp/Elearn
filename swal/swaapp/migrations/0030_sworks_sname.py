# Generated by Django 3.2.3 on 2022-06-26 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0029_sworks_wsname'),
    ]

    operations = [
        migrations.AddField(
            model_name='sworks',
            name='sname',
            field=models.CharField(default=0, max_length=20),
        ),
    ]
