# Generated by Django 3.2.3 on 2022-06-24 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0024_auto_20220623_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='workid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
