# Generated by Django 3.2.3 on 2022-06-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swaapp', '0020_chatting'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatting',
            name='status',
            field=models.CharField(default=0, max_length=10),
        ),
        migrations.AddField(
            model_name='chatting',
            name='subname',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
