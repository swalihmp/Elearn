# Generated by Django 3.2.3 on 2022-06-27 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0032_rename_year_year_ayear'),
    ]

    operations = [
        migrations.CreateModel(
            name='ayear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
                ('dpt', models.CharField(max_length=10)),
                ('tutor', models.CharField(max_length=10)),
                ('createby', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='year',
        ),
    ]
