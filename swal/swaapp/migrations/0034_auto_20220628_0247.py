# Generated by Django 3.2.3 on 2022-06-27 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0033_auto_20220628_0216'),
    ]

    operations = [
        migrations.CreateModel(
            name='academicyear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.RenameModel(
            old_name='ayear',
            new_name='tutors',
        ),
    ]