# Generated by Django 3.2.3 on 2022-05-08 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=50)),
                ('upass', models.CharField(max_length=50)),
                ('ukey', models.CharField(max_length=50)),
            ],
        ),
    ]
